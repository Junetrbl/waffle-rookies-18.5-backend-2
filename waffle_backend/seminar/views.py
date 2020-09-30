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
from .serializers import SeminarSerializer, SimpleSeminarSerializer
from user.models import InstructorProfile, ParticipantProfile
from user.serializers import InstructorProfileSerializer, ParticipantProfileSerializer

class SeminarViewSet(viewsets.GenericViewSet):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer
    permission_classes = (IsAuthenticated(), )

    def get_permissions(self):
        if self.action in ('create', 'login'):
            return (AllowAny(), )
        return self.permission_classes

    def create(self, request):
        seminar_owner = self.request.user

        if seminar_owner.auth.role == "participant":
            return Response({"error": "A Participant cannot open a seminar."}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:            
            seminar = serializer.save()
 

        except IntegrityError:
            return Response("This seminar name already exists.", status=status.HTTP_400_BAD_REQUEST)

        UserSeminar.objects.create(user = seminar_owner, seminar = seminar, role = "instructor")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # PUT /api/v1/seminar/{seminar_id}
    def update(self, request, pk):
        seminar = get_object_or_404(Seminar, pk=pk)
        if request.data == {}:
            return Response("There is no information for edit.", status=status.HTTP_201_CREATED)

        edit_user = self.request.user
        try:
            edit_userseminar = UserSeminar.objects.filter(user__id = edit_user.id, seminar__id = pk)[0]
        except:
            return Response({"error": "Only seminar instructors can edit its information."}, status=status.HTTP_403_FORBIDDEN)

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

        participants_count = UserSeminar.objects.filter(seminar__id = seminar.id, role = "participant").count()
        if int(capacity) < participants_count:
                return Response({"error": "The capacity of a seminar must be larger than the number of its participants"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            update_seminar_serializer = SeminarSerializer(seminar, data=request.data, partial = True)
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT)

        if update_seminar_serializer.is_valid():
            update_seminar_serializer.save()
            return Response(update_seminar_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(update_seminar_serializer.errors, status=status.HTTP_409_CONFLICT)

    # GET /api/v1/seminar/{seminar_id}
    def retrieve(self, request, pk):
        seminar = get_object_or_404(Seminar, pk=pk)

        return Response(SeminarSerializer(seminar).data, status=status.HTTP_200_OK)
    
    # GET /api/v1/seminar/
    def get(self, request):
        name = request.GET.get('name', "")
        seminars = Seminar.objects.filter(name__contains = name)

        order = request.GET.get('order', None)
        
        if order == "earlist":
            sorted_seminars = sorted(seminars, key=lambda x: x.created_at, reverse=False)
        else:
            sorted_seminars = sorted(seminars, key=lambda x: x.created_at, reverse=True)

        return Response(SimpleSeminarSerializer(sorted_seminars, many=True).data, status=status.HTTP_200_OK)


    # @action(detail=False, methods=['POST'])
    # def participant(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')

    #     user = authenticate(request, username=username, password=password)

    #     if user:
    #         login(request, user)
    #         user_serializer = UserSerializer(user, data= request.data) 
    #         # auth = request.data.get('auth')
    #         auth_obj = UserAuth.objects.get(user=user)

    #         if auth_obj.role== "participant":
    #             return Response({"error": "A Participant cannot add his own new role."}, status=status.HTTP_400_BAD_REQUEST)
    #         elif (auth_obj.role== "instructor") ^ (auth_obj.role== "participant and instructor"):
    #             UserAuth.objects.filter(user = user).update(role = "participant and instructor")
    #             auth_obj.save()

    #             participant_data = request.data.get('participant')
    #             ParticipantProfile.objects.update_or_create(user = user, defaults=participant_data)

    #         if user_serializer.is_valid(): 
    #             user_serializer.save()   
    #             return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #     return Response({"error": "Wrong username or wrong password"}, status=status.HTTP_403_FORBIDDEN)

    # @action(detail=False, methods=['POST'])
    # def logout(self, request):
    #     logout(request)
    #     return Response()

    # def retrieve(self, request, pk=None):
    #     user = request.user if pk == 'me' else self.get_object()
    #     return Response(self.get_serializer(user).data)

    # def update(self, request, pk=None):
    #     if pk != 'me':
    #         return Response({"error": "Can't update other Users information"}, status=status.HTTP_403_FORBIDDEN)

    #     user = request.user

    #     serializer = self.get_serializer(user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.update(user, serializer.validated_data)
    #     return Response(serializer.data)
