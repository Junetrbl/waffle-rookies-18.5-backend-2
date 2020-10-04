from .models import Seminar, UserSeminar
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from user.serializers import InstructorProfileSerializer, ParticipantProfileSerializer, UserSerializer, SimpleUserSerializer
from user.models import InstructorProfile, ParticipantProfile

class UserSeminarSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()

    class Meta:
        model = UserSeminar
        # fields = '__all__'
        exclude = ('id', 'role', 'seminar', 'created_at', 'updated_at')
        field = (
            'user',
        )

class SeminarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 200, required = True)
    capacity = serializers.IntegerField(required = True)
    online = serializers.BooleanField(required = False)
    instructors = serializers.SerializerMethodField()
    participants = serializers.SerializerMethodField()
    time = serializers.TimeField(format = '%H:%M', input_formats = ['%H:%M'])

    class Meta:
        model = Seminar
        # exclude = ('created_at', 'updated_at',)
        fields = (
            'id',
            'name',
            'capacity',
            'count',
            'time',
            'online',
            'instructors',
            'participants',
        )
    
    def get_instructors(self, seminar):
        userseminars = UserSeminar.objects.filter(seminar=seminar, role='instructor').select_related('user').values()
        users = []

        for user in userseminars:
            users.append(User.objects.get(id=user['user_id']))

        return SimpleUserSerializer(users, many=True).data

    def get_participants(self, seminar):
        userseminars = UserSeminar.objects.filter(seminar=seminar, role='participant').select_related('user').values()
        users = []

        for user in userseminars:
            users.append(User.objects.get(id=user['user_id']))

        return SimpleUserSerializer(users, many=True).data

    

    def create(self, validated_data):
        seminar = Seminar.objects.create(**validated_data)

        return seminar

class SimpleSeminarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 200, required = True)

    instructors = serializers.SerializerMethodField(required=False)
    participant_count = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Seminar
        exclude = ('created_at', 'updated_at','capacity', 'count', 'time', 'online')
        field = (
            'id',
            'name',
            'instructors',
            'participant_count',
        )
    
    def get_instructors(self, seminar):
        userseminars = UserSeminar.objects.filter(seminar=seminar, role='instructor').select_related('user').values()
        users = []

        for user in userseminars:
            users.append(User.objects.get(id=user['user_id']))

        return SimpleUserSerializer(users, many=True).data
    
    def get_participant_count(self, seminar):
        participant_count = UserSeminar.objects.filter(seminar__id = seminar.id, role = "participant", is_active = True).count()

        return participant_count
    

    def create(self, validated_data):
        seminar = Seminar.objects.create(**validated_data)

        return seminar


class ActiveSeminarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 200, required = True)
    capacity = serializers.IntegerField(required = True)
    online = serializers.BooleanField(required = False)
    instructors = serializers.SerializerMethodField(required=False)
    participants = serializers.SerializerMethodField(required=False)
    time = serializers.TimeField(format = '%H:%M', input_formats = ['%H:%M'])

    class Meta:
        model = Seminar
        exclude = ('created_at', 'updated_at',)
        fields = (
            'id',
            'name',
            'capacity',
            'count',
            'time',
            'online',
            'instructors',
            'participants',
        )
    
    def get_instructors(self, seminar):
        userseminars = UserSeminar.objects.filter(seminar=seminar, role='instructor').select_related('user').values()
        users = []

        for user in userseminars:
            users.append(User.objects.get(id=user['user_id']))

        return SimpleUserSerializer(users, many=True).data

    def get_participants(self, seminar):
        userseminars = UserSeminar.objects.filter(seminar=seminar, role='participant').select_related('user').values()
        users = []

        for user in userseminars:
            users.append(User.objects.get(id=user['user_id']))

        return SimpleUserSerializer(users, many=True).data

    

    def create(self, validated_data):
        seminar = Seminar.objects.create(**validated_data)

        return seminar

