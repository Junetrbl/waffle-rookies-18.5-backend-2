from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Seminar, UserSeminar
from .serializers import SeminarSerializer
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
            return Response("IntegrityError", status=status.HTTP_400_BAD_REQUEST)

        UserSeminar.objects.create(user = seminar_owner, seminar = seminar, role = "instructor")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # @action(detail=False, methods=['PUT'])
    # def login(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')

    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         login(request, user)

    #         data = self.get_serializer(user).data
    #         token, created = Token.objects.get_or_create(user=user)
    #         data['token'] = token.key
    #         return Response(data)

    #     return Response({"error": "Wrong username or wrong password"}, status=status.HTTP_403_FORBIDDEN)
    
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
