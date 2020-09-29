from .models import Seminar, UserSeminar
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from user.serializers import InstructorProfileSerializer, ParticipantProfileSerializer
from user.models import InstructorProfile, ParticipantProfile


class SeminarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 200, required = True)
    capacity = serializers.IntegerField(required = True)
    count = serializers.IntegerField(required = True)
    time = serializers.TimeField(required = True, format="%H:%M")
    online = serializers.BooleanField(required = False)
    # created_at = serializers.DateTimeField(read_only = True)
    # updated_at = serializers.DateTimeField(read_only = True)
    instructor = InstructorProfileSerializer(many = True, required = False)
    participant = ParticipantProfileSerializer(many = True, required= False)


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
            'instructor',
            'participant',
        )
    
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
        print(time)

        return data
    

    def create(self, validated_data):

        return validated_data

        # auth_data = validated_data.pop('auth')
        # if auth_data['role'] == 'participant':
        #     participant_data = validated_data.pop('participant')
        #     user = User.objects.create(**validated_data)
        #     ParticipantProfile.objects.create(user = user, **participant_data)

        # if auth_data['role'] == 'instructor':
        #     instructor_data = validated_data.pop('instructor')
        #     user = User.objects.create(**validated_data)
        #     InstructorProfile.objects.create(user = user, **instructor_data)

        # if auth_data['role'] == 'participant and instructor':
        #     participant_data = validated_data.pop('participant')
        #     instructor_data = validated_data.pop('instructor')
        #     user = User.objects.create(**validated_data)
        #     InstructorProfile.objects.create(user = user, **instructor_data)
        #     ParticipantProfile.objects.create(user = user, **participant_data)

        # UserAuth.objects.create(user = user, **auth_data)


        # Token.objects.create(user=user)
        # return user
    
    # def update(self, instance, validated_data):
    #     if not validated_data:
    #         return instance
        
    #     auth_data = validated_data.pop('auth')
    #     auth = instance.auth

    #     instance.email = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)

    #     instance.save()

    #     auth.role = auth_data.get(
    #         'role',
    #         auth.role
    #     )
    #     auth.save()

    #     if auth_data['role'] == 'participant':
    #         participant_data = validated_data.pop('participant')
    #         participant = instance.participant
    #         participant.university = participant_data.get(
    #         'university',
    #         participant.university
    #         )
    #         participant.save()

    #     if auth_data['role'] == 'instructor':
    #         instructor_data = validated_data.pop('instructor')
    #         instructor = instance.instructor
    #         instructor.company = instructor_data.get(
    #         'company',
    #         instructor.company
    #         )
    #         instructor.year = instructor_data.get(
    #         'year',
    #         instructor.year
    #         )
    #         instructor.save()
        
    #     if auth_data['role'] == 'participant and instructor':
    #         instructor_data = validated_data.pop('instructor')
    #         instructor = instance.instructor
    #         instructor.company = instructor_data.get(
    #         'company',
    #         instructor.company
    #         )
    #         instructor.year = instructor_data.get(
    #         'year',
    #         instructor.year
    #         )
    #         instructor.save()

    #         participant_data = validated_data.pop('participant')
    #         participant = instance.participant
    #         participant.university = participant_data.get(
    #         'university',
    #         participant.university
    #         )
    #         participant.save()

    #     return instance
        
