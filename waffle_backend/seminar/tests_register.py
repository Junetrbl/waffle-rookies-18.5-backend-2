from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
import json
from user.models import InstructorProfile, ParticipantProfile, UserAuth
from seminar.models import Seminar, UserSeminar
import datetime


class PostSeminarUserTestCase(TestCase):
    client = Client()

    def setUp(self):
        self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "davin111",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "email": "bdv111@snu.ac.kr",
                "role": "participant",
                "university": "서울대학교"
            }),
            content_type='application/json'
        )
        self.participant_token = 'Token ' + Token.objects.get(user__username='davin111').key

        self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "davin1111",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "email": "bdv111@snu.ac.kr",
                "role": "participant",
                "university": "서울대학교",
                "accepted":"False"
            }),
            content_type='application/json'
        )
        self.unaccepted_participant_token = 'Token ' + Token.objects.get(user__username='davin1111').key

        self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "davin999",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "email": "bdv111@snu.ac.kr",
                "role": "instructor",
                "year":"1"
            }),
            content_type='application/json'
        )
        self.instructor_token = 'Token ' + Token.objects.get(user__username='davin999').key

        self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "davin1919",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "role" : "instructor",
                "email": "bdv111@snu.ac.kr",
                "year":"1"
            }),
            content_type='application/json'
        )
        self.instructor_token_2 = 'Token ' + Token.objects.get(user__username='davin1919').key

        self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "davin",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "email": "bdv111@snu.ac.kr",
                "role": "instructor",
                "company": "SNU"
            }),
            content_type='application/json'
        )
        self.participant_instructor_token = 'Token ' + Token.objects.get(user__username='davin').key

        response = self.client.post(
            '/api/v1/user/participant/',
            json.dumps({
                "university": "서울대학교",
                "accepted":'True'
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION= self.participant_instructor_token
        )

           


    def test_post_userseminar(self):

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar101",
                "capacity": "2",
                "count": "10",
                "time":"12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        
        )
            
        data = response.json()
        seminar1_id = int(data['id'])

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar102",
                "capacity": "1",
                "count": "10",
                "time":"12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_instructor_token        
        )

        data = response.json()
        seminar2_id = int(data['id'])

        ###no role user
        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token_2
            )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


        ###no_id
        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id+100)),
            json.dumps({
                "role": "instructor"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id+100)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token        
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        ###accepted false
        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.unaccepted_participant_token      
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        ###no profile
        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            json.dumps({
                "role": "instructor"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token    
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        ###one participant participates two seminars
        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar2_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token    
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Seminar102")
        self.assertEqual(data["capacity"], 1)
        self.assertEqual(data["count"], 10)
        self.assertEqual(data["time"], "12:00")
        self.assertTrue(data["online"])

        self.assertEqual(len(data["instructors"]), 1)
        instructor = data["instructors"][0]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["username"], "davin")
        self.assertIn("date_joined", instructor)

        self.assertEqual(len(data["participants"]), 1)
        participant = data["participants"][0]
        self.assertIsNotNone(participant)
        self.assertIn("id", participant)
        self.assertEqual(participant["username"], "davin111")
        self.assertIn("date_joined", participant)

        seminar = Seminar.objects.get(name='Seminar102')
        self.assertEqual(seminar.capacity, 1)
        self.assertEqual(seminar.count, 10)
        self.assertEqual(seminar.time, datetime.time(12, 0))

        ###one person participates and manages one seminar
        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar2_id)),
            json.dumps({
                "role": "instructor"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_instructor_token    
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        ###full seminar
        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar2_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_instructor_token
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        ###one person participates and manages each

        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_instructor_token
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_userseminar(self):
        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar101",
                "capacity": "2",
                "count": "10",
                "time":"12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        
        )
            
        data = response.json()
        seminar1_id = int(data['id'])

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar102",
                "capacity": "1",
                "count": "10",
                "time":"12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_instructor_token        
        )

        data = response.json()
        seminar2_id = int(data['id'])

        self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token
        )

        self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar2_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token    
        )

        self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_instructor_token
        )

        ###no seminar ID
        response = self.client.delete(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id+100)),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token
            )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        ###not a participant
        response = self.client.delete(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.unaccepted_participant_token
            )

        self.assertEqual(len(response.json()), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        ###instructor cannot drop
        response = self.client.delete(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token
            )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        ###successful drop
        response = self.client.delete(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_instructor_token
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data["participants"]), 2)
        participant = data["participants"][1]
        self.assertIsNotNone(participant)
        self.assertIn("id", participant)
        self.assertEqual(participant["username"], "davin")
        self.assertIn("joined_at", participant)
        self.assertIn("dropped_at", participant)
        self.assertFalse(participant["is_active"])

        left_participant = data["participants"][0]
        self.assertEqual(left_participant["username"], "davin111")
        self.assertEqual(left_participant['dropped_at'], None)
        self.assertTrue(left_participant["is_active"])

        ###after drop, one cannot participate again
        response = self.client.post(
            '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
            json.dumps({
                "role": "participant"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_instructor_token
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        ###reduce capacity without considering dropped participants
        response = self.client.put(
            '/api/v1/seminar/{}/'.format(str(seminar1_id)),
            json.dumps({
                "capacity": "1",
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token
            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["capacity"], 1)

        self.assertEqual(len(data["participants"]), 2)



        # response = self.client.post(
        #     '/api/v1/seminar/{}/user/'.format(str(seminar1_id)),
        #     content_type='application/json',
        #     HTTP_AUTHORIZATION = self.instructor_token_2
        #     )

        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    

