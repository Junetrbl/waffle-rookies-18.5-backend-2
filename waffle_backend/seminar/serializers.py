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
    count = serializers.IntegerField(required = True)
    time = serializers.TimeField(required = True, format="%H:%M")
    online = serializers.BooleanField(required = False)
    instructors = serializers.SerializerMethodField(required=False)
    participants = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Seminar
        exclude = ('created_at', 'updated_at',)
        field = (
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
        userseminars = UserSeminar.objects.filter(seminar__id = seminar.id)
        
        instructors = []

        for userseminar in userseminars:
            if (userseminar.role == "instructor"):
                instructors.append(userseminar)

        users = []
        for userlist in UserSeminarSerializer(instructors, many=True).data:
            users.append(userlist.popitem(last=False)[1])

        return SimpleUserSerializer(users, many=True).data

    def get_participants(self, seminar):
        userseminars = UserSeminar.objects.filter(seminar__id = seminar.id)
        
        participants = []

        for userseminar in userseminars:
            if (userseminar.role == "participant"):
                participants.append(userseminar)

        users = []
        for userlist in UserSeminarSerializer(participants, many=True).data:
            users.append(userlist.popitem(last=False)[1])

        return SimpleUserSerializer(users, many=True).data

    def validate(self, data):
        name = data.get('name')
        capacity = data.get('capacity')
        count = data.get('count')
        time = data.get('time')


        if name == "":
            raise serializers.ValidationError("Seminar name is necessary.")
        if capacity <= 0:
            raise serializers.ValidationError("Seminar capacity must be larger than zero.")
        if count <= 0:
            raise serializers.ValidationError("Seminar count must be larger than zero.")
        
        return data
    

    def create(self, validated_data):
        # print("Serializer.create")
        # name = validated_data.pop('name')
        # print(name)
        seminar = Seminar.objects.create(**validated_data)
        # print(seminar)

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
        userseminars = UserSeminar.objects.filter(seminar__id = seminar.id)
        
        instructors = []

        for userseminar in userseminars:
            if (userseminar.role == "instructor"):
                instructors.append(userseminar)

        users = []
        for userlist in UserSeminarSerializer(instructors, many=True).data:
            users.append(userlist.popitem(last=False)[1])

        return SimpleUserSerializer(users, many=True).data
    
    def get_participant_count(self, seminar):
        participant_count = UserSeminar.objects.filter(seminar__id = seminar.id, role = "participant", is_active = True).count()

        return participant_count

    def validate(self, data):
        name = data.get('name')
        capacity = data.get('capacity')
        count = data.get('count')
        time = data.get('time')


        if name == "":
            raise serializers.ValidationError("Seminar name is necessary.")
        if capacity <= 0:
            raise serializers.ValidationError("Seminar capacity must be larger than zero.")
        if count <= 0:
            raise serializers.ValidationError("Seminar count must be larger than zero.")
        
        return data
    

    def create(self, validated_data):
        # print("Serializer.create")
        # name = validated_data.pop('name')
        # print(name)
        seminar = Seminar.objects.create(**validated_data)
        # print(seminar)

        return seminar


class ActiveSeminarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 200, required = True)
    capacity = serializers.IntegerField(required = True)
    count = serializers.IntegerField(required = True)
    time = serializers.TimeField(required = True, format="%H:%M")
    online = serializers.BooleanField(required = False)
    instructors = serializers.SerializerMethodField(required=False)
    participants = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Seminar
        exclude = ('created_at', 'updated_at',)
        field = (
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
        userseminars = UserSeminar.objects.filter(seminar__id = seminar.id)
        
        instructors = []

        for userseminar in userseminars:
            if (userseminar.role == "instructor"):
                instructors.append(userseminar)

        users = []
        for userlist in UserSeminarSerializer(instructors, many=True).data:
            users.append(userlist.popitem(last=False)[1])

        return SimpleUserSerializer(users, many=True).data

    def get_participants(self, seminar):
        userseminars = UserSeminar.objects.filter(seminar__id = seminar.id, is_active = True)
        
        participants = []

        for userseminar in userseminars:
            if (userseminar.role == "participant"):
                participants.append(userseminar)

        users = []
        for userlist in UserSeminarSerializer(participants, many=True).data:
            users.append(userlist.popitem(last=False)[1])

        return SimpleUserSerializer(users, many=True).data

    def validate(self, data):
        name = data.get('name')
        capacity = data.get('capacity')
        count = data.get('count')
        time = data.get('time')


        if name == "":
            raise serializers.ValidationError("Seminar name is necessary.")
        if capacity <= 0:
            raise serializers.ValidationError("Seminar capacity must be larger than zero.")
        if count <= 0:
            raise serializers.ValidationError("Seminar count must be larger than zero.")
        
        return data
    

    def create(self, validated_data):
        # print("Serializer.create")
        # name = validated_data.pop('name')
        # print(name)
        seminar = Seminar.objects.create(**validated_data)
        # print(seminar)

        return seminar

