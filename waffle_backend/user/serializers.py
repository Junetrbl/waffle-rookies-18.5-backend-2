from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import ParticipantProfile, InstructorProfile, UserAuth
from seminar.models import Seminar, UserSeminar

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        exclude = ('user', )
        field = (
            'role',
        )
    def validate_role(self, data):
        auth_user = data
        if not (auth_user == 'instructor' ) and not (auth_user == 'participant'):
            raise serializers.ValidationError("Put proper User role.")
        return data

class LargerParticipantProfileSerializer(serializers.ModelSerializer):
    seminars = serializers.SerializerMethodField(required=False)

    class Meta:
        model = ParticipantProfile
        exclude = ('user', 'created_at', 'updated_at')
        field = (
            'university',
            'accepted',
            'seminars',
        )
     
    def get_seminars(self, profile):
        user = profile.user

        userseminars = UserSeminar.objects.filter(user__id = user.id)
        
        seminars = []

        for userseminar in userseminars:
            if (userseminar.role == "participant"):
                seminars.append(userseminar)

        return MyUserSeminarSerializer(seminars, many=True).data

class LargerInstructorProfileSerializer(serializers.ModelSerializer):
    charge = serializers.SerializerMethodField(required=False)

    class Meta:
        model = InstructorProfile
        exclude = ('user', )
        field = (
            'company',
            'year',
            'charge',
        )
     
    def get_charge(self, profile):
        user = profile.user

        userseminars = UserSeminar.objects.filter(user__id = user.id)
        
        seminars = []

        for userseminar in userseminars:
            if (userseminar.role == "instructor"):
                seminars.append(userseminar)

        return MyUserSeminarSerializer(seminars, many=True).data


class MyUserSeminarSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    joined_at = serializers.DateTimeField(read_only = True)
    is_active = serializers.BooleanField()
    dropped_at = serializers.DateTimeField()

    class Meta:
        model = UserSeminar

        field = (
            'id',
            'name',
            'joined_at',
            'is_active',
            'dropped_at'
        )
    def get_id(self, userseminar):
        return userseminar.seminar.id

    def get_name(self, userseminar):
        return userseminar.seminar.name



class ParticipantProfileSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only = True)

    class Meta:
        model = ParticipantProfile
        exclude = ('user', )
        field = (
            'university',
            'accepted',
            'created_at',
            'updated_at'
        )

class InstructorProfileSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only = True)

    class Meta:
        model = InstructorProfile
        exclude = ('user', )
        field = (
            'company',
            'year',
            'created_at',
            'updated_at',
        )
    
    def validate_year(self, data):
        if data:
            if data<=0:
                raise serializers.ValidationError("Put proper working period.")
        return data

        

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    auth = AuthSerializer(write_only = True)
    participant = ParticipantProfileSerializer(required = False, allow_null = True)
    instructor = InstructorProfileSerializer(required = False, allow_null = True)

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
            'auth',
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
    

    def create(self, validated_data):
        auth_data = validated_data.pop('auth')
        if auth_data['role'] == 'participant':
            participant_data = validated_data.pop('participant')
            user = User.objects.create(**validated_data)
            ParticipantProfile.objects.create(user = user, **participant_data)

        if auth_data['role'] == 'instructor':
            instructor_data = validated_data.pop('instructor')
            user = User.objects.create(**validated_data)
            InstructorProfile.objects.create(user = user, **instructor_data)

        if auth_data['role'] == 'participant and instructor':
            participant_data = validated_data.pop('participant')
            instructor_data = validated_data.pop('instructor')
            user = User.objects.create(**validated_data)
            InstructorProfile.objects.create(user = user, **instructor_data)
            ParticipantProfile.objects.create(user = user, **participant_data)

        UserAuth.objects.create(user = user, **auth_data)


        Token.objects.create(user=user)
        return user
    
    def update(self, instance, validated_data):
        if not validated_data:
            return instance
        
        auth_data = validated_data.pop('auth')
        auth = instance.auth

        instance.email = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()

        auth.role = auth_data.get(
            'role',
            auth.role
        )
        auth.save()

        if auth_data['role'] == 'participant':
            participant_data = validated_data.pop('participant')
            participant = instance.participant
            participant.university = participant_data.get(
            'university',
            participant.university
            )
            participant.save()

        if auth_data['role'] == 'instructor':
            instructor_data = validated_data.pop('instructor')
            instructor = instance.instructor
            instructor.company = instructor_data.get(
            'company',
            instructor.company
            )
            instructor.year = instructor_data.get(
            'year',
            instructor.year
            )
            instructor.save()
        
        if auth_data['role'] == 'participant and instructor':
            instructor_data = validated_data.pop('instructor')
            instructor = instance.instructor
            instructor.company = instructor_data.get(
            'company',
            instructor.company
            )
            instructor.year = instructor_data.get(
            'year',
            instructor.year
            )
            instructor.save()

            participant_data = validated_data.pop('participant')
            participant = instance.participant
            participant.university = participant_data.get(
            'university',
            participant.university
            )
            participant.save()

        return instance

    # def to_representation(self, instance):
    #     representation = super(UserSerializer, self).to_representation(instance)
    #     representation['participant'] = UserSerializer(instance.participant.all()).data
    #     return representation

class SimpleUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'date_joined',
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
    

    def create(self, validated_data):
        auth_data = validated_data.pop('auth')
        if auth_data['role'] == 'participant':
            participant_data = validated_data.pop('participant')
            user = User.objects.create(**validated_data)
            ParticipantProfile.objects.create(user = user, **participant_data)

        if auth_data['role'] == 'instructor':
            instructor_data = validated_data.pop('instructor')
            user = User.objects.create(**validated_data)
            InstructorProfile.objects.create(user = user, **instructor_data)

        if auth_data['role'] == 'participant and instructor':
            participant_data = validated_data.pop('participant')
            instructor_data = validated_data.pop('instructor')
            user = User.objects.create(**validated_data)
            InstructorProfile.objects.create(user = user, **instructor_data)
            ParticipantProfile.objects.create(user = user, **participant_data)

        UserAuth.objects.create(user = user, **auth_data)


        Token.objects.create(user=user)
        return user
    
    def update(self, instance, validated_data):
        if not validated_data:
            return instance
        
        auth_data = validated_data.pop('auth')
        auth = instance.auth

        instance.email = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()

        auth.role = auth_data.get(
            'role',
            auth.role
        )
        auth.save()

        if auth_data['role'] == 'participant':
            participant_data = validated_data.pop('participant')
            participant = instance.participant
            participant.university = participant_data.get(
            'university',
            participant.university
            )
            participant.save()

        if auth_data['role'] == 'instructor':
            instructor_data = validated_data.pop('instructor')
            instructor = instance.instructor
            instructor.company = instructor_data.get(
            'company',
            instructor.company
            )
            instructor.year = instructor_data.get(
            'year',
            instructor.year
            )
            instructor.save()
        
        if auth_data['role'] == 'participant and instructor':
            instructor_data = validated_data.pop('instructor')
            instructor = instance.instructor
            instructor.company = instructor_data.get(
            'company',
            instructor.company
            )
            instructor.year = instructor_data.get(
            'year',
            instructor.year
            )
            instructor.save()

            participant_data = validated_data.pop('participant')
            participant = instance.participant
            participant.university = participant_data.get(
            'university',
            participant.university
            )
            participant.save()

        return instance




class MyUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    last_login = serializers.DateTimeField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    auth = AuthSerializer(write_only = True)
    participant = LargerParticipantProfileSerializer(required = False, allow_null = True)
    instructor = LargerInstructorProfileSerializer(required = False, allow_null = True)

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
            'auth',
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
    

    def create(self, validated_data):
        auth_data = validated_data.pop('auth')
        if auth_data['role'] == 'participant':
            participant_data = validated_data.pop('participant')
            user = User.objects.create(**validated_data)
            ParticipantProfile.objects.create(user = user, **participant_data)

        if auth_data['role'] == 'instructor':
            instructor_data = validated_data.pop('instructor')
            user = User.objects.create(**validated_data)
            InstructorProfile.objects.create(user = user, **instructor_data)

        if auth_data['role'] == 'participant and instructor':
            participant_data = validated_data.pop('participant')
            instructor_data = validated_data.pop('instructor')
            user = User.objects.create(**validated_data)
            InstructorProfile.objects.create(user = user, **instructor_data)
            ParticipantProfile.objects.create(user = user, **participant_data)

        UserAuth.objects.create(user = user, **auth_data)


        Token.objects.create(user=user)
        return user
    
    def update(self, instance, validated_data):
        if not validated_data:
            return instance
        
        auth_data = validated_data.pop('auth')
        auth = instance.auth

        instance.email = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()

        auth.role = auth_data.get(
            'role',
            auth.role
        )
        auth.save()

        if auth_data['role'] == 'participant':
            participant_data = validated_data.pop('participant')
            participant = instance.participant
            participant.university = participant_data.get(
            'university',
            participant.university
            )
            participant.save()

        if auth_data['role'] == 'instructor':
            instructor_data = validated_data.pop('instructor')
            instructor = instance.instructor
            instructor.company = instructor_data.get(
            'company',
            instructor.company
            )
            instructor.year = instructor_data.get(
            'year',
            instructor.year
            )
            instructor.save()
        
        if auth_data['role'] == 'participant and instructor':
            instructor_data = validated_data.pop('instructor')
            instructor = instance.instructor
            instructor.company = instructor_data.get(
            'company',
            instructor.company
            )
            instructor.year = instructor_data.get(
            'year',
            instructor.year
            )
            instructor.save()

            participant_data = validated_data.pop('participant')
            participant = instance.participant
            participant.university = participant_data.get(
            'university',
            participant.university
            )
            participant.save()

        return instance