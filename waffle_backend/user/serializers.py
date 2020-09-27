from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import ParticipantProfile, InstructorProfile, Auth


class ParticipantProfileSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only = True)

    class Meta:
        model = ParticipantProfile
        field = (
            'user',
            'university',
            'accepted',
            'created_at',
            'updated_at'
        )

class InstructorProfileSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only = True)

    class Meta:
        model = ParticipantProfile
        field = (
            'user',
            'company',
            'year',
            'created_at',
            'updated_at'
        )

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        field = (
            'user',
            'role'
        )

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    auth = AuthSerializer(many=True, write_only = True)
    participant = ParticipantProfileSerializer(null = True, required = False, allow_null = True)
    instructor = InstructorProfileSerializer(null = True, required = False, allow_null = True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'last_login',
            'date_joined',
            'participant',
            'instructor',
        )

    def validate_password(self, value):
        return make_password(value)

    def validate(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        if bool(first_name) ^ bool(last_name):
            raise serializers.ValidationError("First name and last name should appear together.")
        if first_name and last_name and not (first_name.isalpha() and last_name.isalpha()):
            raise serializers.ValidationError("First name or last name should not have number.")
        return data
    
    def validate_instructor(self, data, instructor):
        instructor_profile = data.get('instructor')
        if instructor_profile.year <= 0:
            raise serializers.ValidationError("Put proper working period.")
        return data
    
    # def validate_auth(self, data, auth):
    #     auths = data.get('auth')
    #     if auths.role != 

    def create(self, validated_data):
        user_role = validated_data.get('auth')
        if user_role.role == 'participant':
            validated_data.instructor = None
        if user_role.role == 'instructor':
            validated_data.participant = None
        user = super(UserSerializer, self).create(validated_data)
        Token.objects.create(user=user)
        return user
