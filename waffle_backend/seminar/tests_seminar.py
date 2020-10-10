from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
import json
from user.models import InstructorProfile, ParticipantProfile, UserAuth
from seminar.models import Seminar, UserSeminar
import datetime


class PostSeminarTestCase(TestCase):
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
                "email": "bdv111@snu.ac.kr",
                "role": "instructor",
                "year":"1"
            }),
            content_type='application/json'
        )
        self.instructor_token_2 = 'Token ' + Token.objects.get(user__username='davin1919').key


    def test_post_seminar_incomplete_request(self):
        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "count": "10",
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "capacity": "2",
                "count": "10",
                "time": "12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "count": "10",
                "time": "12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "time": "12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)



    def test_post_seminar_wrong_info(self):
        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "",
                "capacity": "2",
                "count":"10",
                "time": "12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "-10",
                "count":"10",
                "time": "12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        
            )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "count":"-10",
                "time": "12:00"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "count":"10",
                "time": "12:00:36"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)


    def test_post_seminar_online(self):
        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "count": "10",
                "time":"12:00",
                "online":"FALSE"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Seminar1")
        self.assertEqual(data["capacity"], 2)
        self.assertEqual(data["count"], 10)
        self.assertEqual(data["time"], "12:00")
        self.assertFalse(data["online"])

        instructor = data["instructors"][0]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["username"], "davin999")
        self.assertEqual(instructor["email"], "bdv111@snu.ac.kr")
        self.assertEqual(instructor["first_name"], "Davin")
        self.assertEqual(instructor["last_name"], "Byeon")
        self.assertIn("date_joined", instructor)

        self.assertEqual(len(data["participants"]), 0)

        seminar = Seminar.objects.get(name='Seminar1')
        self.assertEqual(seminar.time, datetime.time(12, 0))

        response = response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "count": "10",
                "time":"12:00",
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token_2        
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        self.assertTrue(data["online"])

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 2)

    def test_post_seminar_participant(self):
        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "count": "10",
                "time":"12:00",
                "online":"false"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token        
            )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        seminar_count = Seminar.objects.count()
        self.assertEqual(seminar_count, 0)
    
    def test_get_instructor(self):
        self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "count": "10",
                "time":"12:00",
                "online":"FALSE"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token        
            )

        response = self.client.get(
            '/api/v1/user/me/',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.instructor_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()  
        instructor = data["instructor"]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["company"], "")
        self.assertEqual(instructor["year"], 1)
        self.assertEqual(len(instructor["charge"]), 1)
        self.assertIn("joined_at", instructor["charge"][0])



class PutSeminarTestCase(TestCase):
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
                "email": "bdv111@snu.ac.kr",
                "role": "instructor",
                "year":"1"
            }),
            content_type='application/json'
        )
        self.instructor_token_2 = 'Token ' + Token.objects.get(user__username='davin1919').key


        
    def test_put_seminar_incomplete_request(self):
        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "2",
                "count": "10",
                "time":"12:00",
                "online":"FALSE"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token
        )
        data = response.json()  

        seminar_id = int(data['id'])

        response = self.client.put(
            '/api/v1/seminar/{}/'.format(str(seminar_id)),
            json.dumps({
                # empty body
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token
            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put(
            '/api/v1/seminar/{}/'.format(str(seminar_id+100)),
            json.dumps({
                # empty body
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token
            
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.put(
            '/api/v1/seminar/{}/'.format(str(seminar_id)),
            json.dumps({
                # empty body
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.participant_token       
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.put(
            '/api/v1/seminar/{}/'.format(str(seminar_id)),
            json.dumps({
                # empty body
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token_2       
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.put(
            '/api/v1/seminar/{}/'.format(str(seminar_id)),
            json.dumps({
                "name": "THIS IS SEMINAR!!!!!!",
                "capacity": "100",
                "count": "100",
                "time":"00:00",
                "online":"T"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token
            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "THIS IS SEMINAR!!!!!!")
        self.assertEqual(data["capacity"], 100)
        self.assertEqual(data["count"], 100)
        self.assertTrue(data["online"])
        seminar = Seminar.objects.get(name='THIS IS SEMINAR!!!!!!')
        self.assertEqual(seminar.time, datetime.time(0, 0))

        instructor = data["instructors"][0]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["username"], "davin999")
        self.assertEqual(instructor["email"], "bdv111@snu.ac.kr")
        self.assertEqual(instructor["first_name"], "Davin")
        self.assertEqual(instructor["last_name"], "Byeon")
        self.assertIn("date_joined", instructor)

        self.assertEqual(len(data["participants"]), 0)

class GetSeminarTestCase(TestCase):
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
                "email": "bdv111@snu.ac.kr",
                "role": "instructor",
                "year":"1"
            }),
            content_type='application/json'
        )
        self.instructor_token_2 = 'Token ' + Token.objects.get(user__username='davin1919').key
        
    def test_get_seminar(self):
        self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar1",
                "capacity": "1",
                "count": "10",
                "time":"12:00",
                "online":"FALSE"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token
        )

        response = self.client.post(
            '/api/v1/seminar/',
            json.dumps({
                "name": "Seminar2",
                "capacity": "2",
                "count": "10",
                "time":"12:00",
                "online":"True"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token_2
        )
        data = response.json()  

        seminar_id = int(data['id'])

        response = self.client.get(
            '/api/v1/seminar/{}/'.format(str(seminar_id+100)),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token           
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(
            '/api/v1/seminar/{}/'.format(str(seminar_id)),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token           
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Seminar2")
        self.assertEqual(data["capacity"], 2)
        self.assertEqual(data["count"], 10)
        self.assertTrue(data["online"])
        seminar = Seminar.objects.get(name='Seminar2')
        self.assertEqual(seminar.time, datetime.time(12, 0))

        instructor = data["instructors"][0]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["username"], "davin1919")
        self.assertEqual(instructor["email"], "bdv111@snu.ac.kr")
        self.assertEqual(instructor["first_name"], "Davin")
        self.assertEqual(instructor["last_name"], "Byeon")
        self.assertIn("date_joined", instructor)

        self.assertEqual(len(data["participants"]), 0)

        response = self.client.get(
            '/api/v1/seminar/'.format(str(seminar_id)),
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token           
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(len(data), 2)
        for i in data:
            self.assertIn("id", i)
            self.assertIn("name", i)

            instructor = i["instructors"][0]
            self.assertIsNotNone(instructor)
            self.assertIn("id", instructor)
            self.assertIn("username", instructor)
            self.assertEqual(instructor["email"], "bdv111@snu.ac.kr")
            self.assertEqual(instructor["first_name"], "Davin")
            self.assertEqual(instructor["last_name"], "Byeon")
            self.assertIn("date_joined", instructor)

            self.assertEqual(i['participant_count'], 0)
        
        ###name param       
        response = self.client.get(
            '/api/v1/seminar/?name=Seminar1',
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token           
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(len(data), 1)

        ###wrong name param
        response = self.client.get(
            '/api/v1/seminar/?name=SuperFunSeminar',
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token           
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(len(data), 0)

        ###earliest order
        response = self.client.get(
            '/api/v1/seminar/?order=earliest',
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token           
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        first_seminar = data[0]
        second_seminar = data[1]

        self.assertEqual(first_seminar["name"], "Seminar1")
        self.assertEqual(second_seminar["name"], "Seminar2")

        ###wrond order
        response = self.client.get(
            '/api/v1/seminar/?order=oldest',
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token           
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        first_seminar = data[0]
        second_seminar = data[1]

        self.assertEqual(first_seminar["name"], "Seminar2")
        self.assertEqual(second_seminar["name"], "Seminar1")

        ###wrong param
        response = self.client.get(
            '/api/v1/seminar/?count=2',
            content_type='application/json',
            HTTP_AUTHORIZATION = self.instructor_token           
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        first_seminar = data[0]
        second_seminar = data[1]

        self.assertEqual(first_seminar["name"], "Seminar2")
        self.assertEqual(second_seminar["name"], "Seminar1")