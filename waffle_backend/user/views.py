from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import UserAuth
from user.serializers import UserSerializer, MyUserSerializer
from .models import ParticipantProfile

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated(), )

    def get_permissions(self):
        if self.action in ('create', 'login'):
            return (AllowAny(), )
        return self.permission_classes

    def create(self, request):

        try:
            role = request.data.get('role')

            if not (role == 'instructor' ) and not (role == 'participant'):
                return Response({"error": "Put proper role"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        try:
            year = request.data.get('year')
            if year<=0:
                return Response({"error": "Workind period must be larger than zero."}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = serializer.save()
        except IntegrityError:
            return Response({"error": "A user with that username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        login(request, user)

        data = serializer.data
        data['token'] = user.auth_token.key
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['PUT'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            data = self.get_serializer(user).data
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            return Response(data)

        return Response({"error": "Wrong username or wrong password"}, status=status.HTTP_403_FORBIDDEN)
    
    @action(detail=False, methods=['POST'])
    def participant(self, request):
        user = request.user

        if user:
            login(request, user)
            user_serializer = self.get_serializer(user, data=request.data, partial=True)

            auth_obj = UserAuth.objects.get(user=user)

            if auth_obj.role== "participant" or auth_obj.role== "participant and instructor":
                return Response({"error": "A Participant cannot add his own new role."}, status=status.HTTP_400_BAD_REQUEST)
            elif (auth_obj.role== "instructor"):
                auth_obj.role = "participant and instructor"
                auth_obj.save()

                participant_data = request.data.get('participant')
                ParticipantProfile.objects.update_or_create(user = user, defaults=participant_data)
                print()
            
            if user_serializer.is_valid(): 
                user_serializer.save()   
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        return Response({"error": "Wrong username or wrong password"}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=False, methods=['POST'])
    def logout(self, request):
        logout(request)
        return Response()

    def retrieve(self, request, pk=None):
        user = request.user if pk == 'me' else self.get_object()
        
        return Response(MyUserSerializer(user).data)

    def update(self, request, pk=None):
        if pk != 'me':
            return Response({"error": "Can't update other Users information"}, status=status.HTTP_403_FORBIDDEN)

        user = request.user

        role = request.data.get('role')
        if not (role == 'instructor' ) and not (role == 'participant') and not (role == None):
            return Response({"error": "Put proper role"}, status=status.HTTP_400_BAD_REQUEST)


        year = request.data.get('year')
        if year == None:
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.update(user, serializer.validated_data)
            return Response(serializer.data)
        elif year <= 0:
            return Response({"error": "Workind period must be larger than zero."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.update(user, serializer.validated_data)
        return Response(serializer.data)
