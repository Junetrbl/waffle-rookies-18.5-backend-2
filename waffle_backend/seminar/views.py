from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Seminar, UserSeminar
from .serializers import SeminarSerializer, SimpleSeminarSerializer, ActiveSeminarSerializer
from user.models import InstructorProfile, ParticipantProfile
from user.serializers import InstructorProfileSerializer, ParticipantProfileSerializer
import datetime
from rest_framework.authentication import TokenAuthentication
from django.core.cache import cache


class SeminarViewSet(viewsets.GenericViewSet):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer
    permission_classes = (IsAuthenticated(), )

    def get_permissions(self):
        if self.action in ('create', 'update', 'retrieve', 'get', 'user'):
            return (IsAuthenticated(), )
        return self.permission_classes

    def create(self, request):
        seminar_owner = self.request.user

        if seminar_owner.auth.role == "participant":
            return Response({"error": "A Participant cannot open a seminar."}, status=status.HTTP_403_FORBIDDEN)

        if UserSeminar.objects.filter(user__id = seminar_owner.id, role = "instructor").count() > 0:
            return Response({"error":"User already manages a seminar."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)

        capacity = request.data.get('capacity')
        count = request.data.get('count')

        if capacity is not None and count is not None:
            if (int(capacity) <= 0) or (int(count)<=0):
                return Response({"error":"It is not proper value for count or capacity."}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            seminar = serializer.save()
            UserSeminar.objects.create(user = seminar_owner, seminar = seminar, role = "instructor")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT /api/v1/seminar/{seminar_id}
    def update(self, request, pk):
        seminar = get_object_or_404(Seminar, pk=pk)

        edit_user = self.request.user
        try:
            edit_userseminar = UserSeminar.objects.filter(user__id = edit_user.id, seminar__id = pk, role = "instructor")[0]
        except:
            return Response({"error": "Only seminar instructors can edit its information."}, status=status.HTTP_403_FORBIDDEN)
        
        if request.data == {}:
            return Response({"error":"There is no information for edit."}, status=status.HTTP_200_OK)

        userseminars = UserSeminar.objects.filter(seminar__id = seminar.id)      
        instructors = []

        for userseminar in userseminars:
            if (userseminar.role == "instructor"):
                instructors.append(userseminar)

        if edit_userseminar not in instructors:
            return Response({"error": "Only seminar instructors can edit its information."}, status=status.HTTP_403_FORBIDDEN)

        name = request.data.get('name')
        capacity = request.data.get('capacity')
        count = request.data.get('count')
        time = request.data.get('time')
        online = request.data.get('online')

        participants_count = UserSeminar.objects.filter(seminar__id = seminar.id, role = "participant", is_active = True).count()
        if int(capacity) < participants_count:
                return Response({"error": "The capacity of a seminar must be larger than the number of its participants"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            update_seminar_serializer = self.get_serializer(seminar, data=request.data, partial = True)
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT)

        if update_seminar_serializer.is_valid():
            update_seminar_serializer.save()
            return Response(update_seminar_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(update_seminar_serializer.errors, status=status.HTTP_409_CONFLICT)

    # GET /api/v1/seminar/{seminar_id}
    def retrieve(self, request, pk):
        seminar = get_object_or_404(Seminar, pk=pk)
        serializer = self.get_serializer(seminar)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # GET /api/v1/seminar/
    def list(self, request):
        name = request.query_params.get('name', "")
        order = request.query_params.get('order', None)

        if name == "": #name이 query param에 없는 경우 cache 사용
            if order == "earliest":
                cache_key = 'seminar_list_earlist' #Cache는 key-value 구조, cache에 맞는 key를 지정
                data = cache.get(cache_key)

                if data is None:
                    print("earliest cache miss")
                    # seminars = self.queryset.filter(name__contains = name)
                    seminars = self.queryset.all()

                    sorted_seminars = seminars.order_by('created_at')

                    data = SimpleSeminarSerializer(sorted_seminars, many=True).data
                    cache.set(cache_key, data, timeout = 300)
                else:
                    print("earliest cache hit")

            else:
                cache_key = 'seminar_list_latest'
                data = cache.get(cache_key)

                if data is None:
                    print("latest cache miss")
                    # seminars = self.queryset.filter(name__contains = name)
                    seminars = self.queryset.all()

                    sorted_seminars = seminars.order_by('-created_at')

                    data = SimpleSeminarSerializer(sorted_seminars, many=True).data
                    cache.set(cache_key, data, timeout = 300)
                else:
                    print("latest cache hit")
        
        else: #name이 query param에 있는 경우 caching 사용하지 않음
            seminars = self.queryset.filter(name__contains = name)

            if order == "earliest":
                sorted_seminars = seminars.order_by('created_at')
            else:
                sorted_seminars = seminars.order_by('-created_at')

            data = SimpleSeminarSerializer(sorted_seminars, many=True).data

        return Response(data, status=status.HTTP_200_OK)

    # POST /api/v1/seminar/{seminar_id}/user
    @action(detail=True, methods=['POST', 'DELETE'])
    def user(self, request, pk):
        seminar = get_object_or_404(Seminar, pk=pk)

        if self.request.method == 'POST':
            register_user = self.request.user

            #role constraints
            role = request.data.get('role')

            if (role != "participant") and (role != "instructor"):
                return Response({"error":"User must be either a participant or an instructor."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if (role == "participant"):
                    profile = ParticipantProfile.objects.filter(user_id = register_user.id)
                    if not profile:
                        return Response({"error": "User must register his own profile."}, status=status.HTTP_403_FORBIDDEN)
                    if profile[0].accepted == False:
                        return Response({"error": "User is not accepted yet."}, status=status.HTTP_403_FORBIDDEN)
                    if UserSeminar.objects.filter(user__id = register_user.id, role = "participant", seminar__id = seminar.id).exists():
                        if not UserSeminar.objects.filter(user__id = register_user.id, role = "participant", seminar__id = seminar.id)[0].is_active:
                            return Response({"error":"User is already dropped this seminar."}, status=status.HTTP_400_BAD_REQUEST)  
                    #capacity constraints    
                    participants_count = UserSeminar.objects.filter(seminar__id = seminar.id, role = "participant", is_active= True).count()

                    if participants_count == seminar.count:           
                        return Response({"error":"This seminar is already full."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    profile = InstructorProfile.objects.filter(user_id = register_user.id)
                    if not profile:
                        return Response({"error": "User must register his own profile."}, status=status.HTTP_403_FORBIDDEN)

                    if UserSeminar.objects.filter(user__id = register_user.id, role = "instructor").exists():
                        return Response({"error":"User already manages a seminar."}, status=status.HTTP_400_BAD_REQUEST)
            

            if UserSeminar.objects.filter(user__id = register_user.id, seminar__id = seminar.id).exists():
                return Response({"error":"User already takes part in the seminar."}, status=status.HTTP_400_BAD_REQUEST)

            UserSeminar.objects.create(user = register_user, seminar = seminar, role = role)
            
            return Response(SeminarSerializer(seminar).data, status=status.HTTP_201_CREATED)
        if self.request.method == "DELETE":
            drop_user = self.request.user
            userseminar = UserSeminar.objects.filter(user__id = drop_user.id, seminar__id = seminar.id)

            if userseminar.count() == 0:
                return Response(request.data, status=status.HTTP_200_OK)

            if userseminar[0].role == "instructor":
                return Response({"error": "Instructor must stay in the seminar.."}, status=status.HTTP_403_FORBIDDEN)

            userseminar.update(is_active = False, dropped_at = datetime.datetime.now())
            userseminar[0].is_active = False
            userseminar[0].dropped_at = datetime.datetime.now()
            seminar.refresh_from_db()
            return Response(ActiveSeminarSerializer(seminar).data, status=status.HTTP_200_OK)
 