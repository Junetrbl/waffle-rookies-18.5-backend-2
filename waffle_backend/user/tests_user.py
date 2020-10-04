from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
import json
from user.models import InstructorProfile, ParticipantProfile, UserAuth


class PostUserTestCase(TestCase):
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

    def test_post_user_duplicated_username(self):
        response = self.client.post(
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
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_post_user_incomplete_request(self):
        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "participant",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "email": "bdv111@snu.ac.kr",
                "role": "wrong_role",
                "university": "서울대학교"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "participant",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "email": "bdv111@snu.ac.kr",
                "university": "서울대학교"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "participant",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "role": "participant",
                "university": "서울대학교"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_post_user(self):
        response = self.client.post(
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
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "participant",
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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["username"], "participant")
        self.assertEqual(data["email"], "bdv111@snu.ac.kr")
        self.assertEqual(data["first_name"], "Davin")
        self.assertEqual(data["last_name"], "Byeon")
        self.assertIn("last_login", data)
        self.assertIn("date_joined", data)
        self.assertIn("token", data)

        participant = data["participant"]
        self.assertIsNotNone(participant)
        self.assertIn("id", participant)
        self.assertEqual(participant["university"], "서울대학교")
        self.assertFalse(participant["accepted"])
        self.assertEqual(len(participant["seminars"]), 0)

        self.assertIsNone(data["instructor"])

        user_count = User.objects.count()
        self.assertEqual(user_count, 2)
        participant_count = ParticipantProfile.objects.count()
        self.assertEqual(participant_count, 2)
        instructor_count = InstructorProfile.objects.count()
        self.assertEqual(instructor_count, 0)


class PutUserMeTestCase(TestCase):
    client = Client()

    def setUp(self):
        self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "part",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "email": "bdv111@snu.ac.kr",
                "role": "participant",
                "university": "서울대학교"
            }),
            content_type='application/json'
        )
        self.participant_token = 'Token ' + Token.objects.get(user__username='part').key

        self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "inst",
                "password": "password",
                "first_name": "Davin",
                "last_name": "Byeon",
                "email": "bdv111@snu.ac.kr",
                "role": "instructor",
                "year": 1
            }),
            content_type='application/json'
        )
        self.instructor_token = 'Token ' + Token.objects.get(user__username='inst').key

    def test_put_user_incomplete_request(self):
        response = self.client.put(
            '/api/v1/user/me/',
            json.dumps({
                "first_name": "Dabin"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(
            '/api/v1/user/me/',
            json.dumps({
                "first_name": "Dabin"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.participant_token
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        participant_user = User.objects.get(username='part')
        self.assertEqual(participant_user.first_name, 'Davin')

        response = self.client.put(
            '/api/v1/user/me/',
            json.dumps({
                "username": "inst123",
                "email": "bdv111@naver.com",
                "company": "매스프레소",
                "year": -1
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.instructor_token
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        instructor_user = User.objects.get(username='inst')
        self.assertEqual(instructor_user.email, 'bdv111@snu.ac.kr')

    def test_put_user_me_participant(self):
        response = self.client.put(
            '/api/v1/user/me/',
            json.dumps({
                "username": "part123",
                "email": "bdv111@naver.com",
                "university": "경북대학교"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.participant_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["username"], "part123")
        self.assertEqual(data["email"], "bdv111@naver.com")
        self.assertEqual(data["first_name"], "Davin")
        self.assertEqual(data["last_name"], "Byeon")
        self.assertIn("last_login", data)
        self.assertIn("date_joined", data)
        self.assertNotIn("token", data)

        participant = data["participant"]
        self.assertIsNotNone(participant)
        self.assertIn("id", participant)
        self.assertEqual(participant["university"], "경북대학교")
        self.assertTrue(participant["accepted"])
        self.assertEqual(len(participant["seminars"]), 0)

        self.assertIsNone(data["instructor"])
        participant_user = User.objects.get(username='part123')
        self.assertEqual(participant_user.email, 'bdv111@naver.com')

    def test_put_user_me_instructor(self):
        response = self.client.put(
            '/api/v1/user/me/',
            json.dumps({
                "username": "inst123",
                "email": "bdv111@naver.com",
                "first_name": "Dabin",
                "last_name": "Byeon",
                "university": "서울대학교",  # this should be ignored
                "company": "매스프레소",
                "year": 2
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION= self.instructor_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["username"], "inst123")
        self.assertEqual(data["email"], "bdv111@naver.com")
        self.assertEqual(data["first_name"], "Dabin")
        self.assertEqual(data["last_name"], "Byeon")
        self.assertIn("last_login", data)
        self.assertIn("date_joined", data)
        self.assertNotIn("token", data)

        self.assertIsNone(data["participant"])

        instructor = data["instructor"]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["company"], "매스프레소")
        self.assertEqual(instructor["year"], 2)
        self.assertIsNone(instructor["charge"])

        instructor_user = User.objects.get(username='inst123')
        self.assertEqual(instructor_user.email, 'bdv111@naver.com')

class PostInstructorTestCase(TestCase):
    client = Client()   

    def test_post_only_first_name(self):
        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "inst1004",
                "password": "password",
                "email":"iteachwell@gmail.com",
                "first_name": "Teacher",
                "role": "instructor",
            }),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_post_negative_year(self):
        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "inst1004",
                "password": "password",
                "email":"iteachwell@gmail.com",
                "first_name": "Teacher",
                "last_name":"Lee",
                "role": "instructor",
                "year": -1
            }),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_post_no_instructor_info(self):
        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "inst1004",
                "password": "password",
                "email":"iteachwell@gmail.com",
                "first_name": "Teacher",
                "last_name":"Lee",
                "role": "instructor",
                "university":"SNU"
            }),
            content_type = 'application/json'
        )
        self.inst1004_token = 'Token ' + Token.objects.get(user__username='inst1004').key

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["username"], "inst1004")
        self.assertEqual(data["email"], "iteachwell@gmail.com")
        self.assertEqual(data["first_name"], "Teacher")
        self.assertEqual(data["last_name"], "Lee")
        self.assertIn("last_login", data)
        self.assertIn("date_joined", data)
        self.assertIn("token", data)

        self.assertIsNone(data["participant"])

        instructor = data["instructor"]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["company"], "")
        self.assertIsNone(instructor["year"])
        self.assertIsNone(instructor["charge"])

        instructor_user = User.objects.get(username='inst1004')
        self.assertEqual(instructor_user.username, "inst1004")
        self.assertEqual(instructor_user.email, "iteachwell@gmail.com")
        self.assertEqual(instructor_user.first_name, "Teacher")
        self.assertEqual(instructor_user.last_name, "Lee")
        self.assertTrue(hasattr(instructor_user, "last_login"))
        self.assertTrue(hasattr(instructor_user, "date_joined"))

        instructor = instructor_user.instructor
        self.assertIsNotNone(instructor)
        self.assertIsNotNone(instructor.id)
        self.assertEqual(instructor.company, "")
        self.assertIsNone(instructor.year)
        self.assertFalse(hasattr(instructor, "charge"))


class LoginInstructorTestCase(TestCase):
    client = Client()

    def setUp(self):
        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "inst1004",
                "password": "password",
                "email":"iteachwell@gmail.com",
                "first_name": "Teacher",
                "last_name":"Lee",
                "role": "instructor",
                "university":"SNU"
            }),
            content_type = 'application/json'
        )
        self.inst1004_token = 'Token ' + Token.objects.get(user__username='inst1004').key

        response = self.client.put(
            '/api/v1/user/login/',
            json.dumps({
                "username": "inst1004",
                "password": "wrongpassword",
            }),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.put(
            '/api/v1/user/login/',
            json.dumps({
                "username": "inst1004",
                "password": "password"
            }),
            content_type = 'application/json'
        )
        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["username"], "inst1004")
        self.assertEqual(data["email"], "iteachwell@gmail.com")
        self.assertEqual(data["first_name"], "Teacher")
        self.assertEqual(data["last_name"], "Lee")
        self.assertIn("last_login", data)
        self.assertIn("date_joined", data)
        self.assertIn("token", data)

        self.assertIsNone(data["participant"])

        instructor = data["instructor"]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["company"], "")
        self.assertIsNone(instructor["year"])
        self.assertIsNone(instructor["charge"])

        instructor_user = User.objects.get(username='inst1004')
        self.assertEqual(instructor_user.username, "inst1004")
        self.assertEqual(instructor_user.email, "iteachwell@gmail.com")
        self.assertEqual(instructor_user.first_name, "Teacher")
        self.assertEqual(instructor_user.last_name, "Lee")
        self.assertTrue(hasattr(instructor_user, "last_login"))
        self.assertTrue(hasattr(instructor_user, "date_joined"))

        instructor = instructor_user.instructor
        self.assertIsNotNone(instructor)
        self.assertIsNotNone(instructor.id)
        self.assertEqual(instructor.company, "")
        self.assertIsNone(instructor.year)
        self.assertFalse(hasattr(instructor, "charge"))


class PutUserMeTestCaseBoth(TestCase):
    client = Client()

    def setUp(self):
        response = self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "inst1004",
                "password": "password",
                "email":"iteachwell@gmail.com",
                "first_name": "Teacher",
                "last_name":"Lee",
                "role": "instructor",
                "university":"SNU"
            }),
            content_type = 'application/json'
        )
        self.inst1004_token = 'Token ' + Token.objects.get(user__username='inst1004').key

    def test_put_user_incomplete_request(self):
        response = self.client.put(
            '/api/v1/user/me/',
            json.dumps({
                "company": "NaKaLi"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(
            '/api/v1/user/me/',
            json.dumps({
                "role" : "manager"
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.inst1004_token
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_user_me_instructor(self):
        response = self.client.put(
            '/api/v1/user/me/',
            json.dumps({
                "company": "NaKaLi",
                "year": 100
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.inst1004_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["username"], "inst1004")
        self.assertEqual(data["email"], "iteachwell@gmail.com")
        self.assertEqual(data["first_name"], "Teacher")
        self.assertEqual(data["last_name"], "Lee")
        self.assertIn("last_login", data)
        self.assertIn("date_joined", data)

        self.assertIsNone(data["participant"])

        instructor = data["instructor"]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["company"], "NaKaLi")
        self.assertEqual(instructor["year"], 100)
        self.assertIsNone(instructor["charge"])

        instructor_user = User.objects.get(username='inst1004')
        self.assertEqual(instructor_user.username, "inst1004")
        self.assertEqual(instructor_user.email, "iteachwell@gmail.com")
        self.assertEqual(instructor_user.first_name, "Teacher")
        self.assertEqual(instructor_user.last_name, "Lee")
        self.assertTrue(hasattr(instructor_user, "last_login"))
        self.assertTrue(hasattr(instructor_user, "date_joined"))

        instructor = instructor_user.instructor
        self.assertIsNotNone(instructor)
        self.assertIsNotNone(instructor.id)
        self.assertEqual(instructor.company, "NaKaLi")
        self.assertEqual(instructor.year, 100)
        self.assertFalse(hasattr(instructor, "charge"))

    def test_post_user_participant(self):
        response = self.client.post(
            '/api/v1/user/participant/',
            json.dumps({
                "university": "서울대학교",
                "accepted":'False'
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION= self.inst1004_token
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = response.json()
        instructor_user = User.objects.get(username='inst1004')
        user = UserAuth.objects.get(user = instructor_user)
        self.assertEqual(user.role, "participant and instructor")

        participant = data["participant"]
        self.assertIsNotNone(participant)
        self.assertIn("id", participant)
        self.assertEqual(participant["university"], "서울대학교")
        self.assertFalse(participant["accepted"])
        self.assertEqual(participant["seminars"], [])

        participant_user = User.objects.get(username='inst1004')

        participant = participant_user.participant
        self.assertIsNotNone(participant)
        self.assertIsNotNone(participant.id)
        self.assertEqual(participant.university, "서울대학교")
        self.assertFalse(participant.accepted)

class GetUserTestCase(TestCase):
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
        self.davin_token = 'Token ' + Token.objects.get(user__username='davin111').key

        self.client.post(
            '/api/v1/user/',
            json.dumps({
                "username": "DJ",
                "password": "password",
                "email":"iteachwell@gmail.com",
                "first_name": "DJ",
                "last_name":"Lee",
                "role": "instructor",
                "company":"LG CNS",
                "year":"1"
            }),
            content_type = 'application/json'
        )
        self.inst1004_token = 'Token ' + Token.objects.get(user__username='DJ').key


    def test_get_unavailable_user(self):
        response = self.client.get(
            '/api/v1/user/100/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user(self):
        davin_id = User.objects.get(username = "davin111")
        response = self.client.get(
            '/api/v1/user/{}/'.format(str(davin_id.id)),
            content_type='application/json',
            HTTP_AUTHORIZATION=self.davin_token

        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["username"], "davin111")
        self.assertEqual(data["email"], "bdv111@snu.ac.kr")
        self.assertEqual(data["first_name"], "Davin")
        self.assertEqual(data["last_name"], "Byeon")
        self.assertIn("last_login", data)
        self.assertIn("date_joined", data)
        self.assertNotIn("token", data)

        participant = data["participant"]
        self.assertIsNotNone(participant)
        self.assertIn("id", participant)
        self.assertEqual(participant["university"], "서울대학교")
        self.assertTrue(participant["accepted"])
        self.assertEqual(len(participant["seminars"]), 0)

        self.assertIsNone(data["instructor"])

        user_count = User.objects.count()
        self.assertEqual(user_count, 2)
        participant_count = ParticipantProfile.objects.count()
        self.assertEqual(participant_count, 1)
        instructor_count = InstructorProfile.objects.count()
        self.assertEqual(instructor_count, 1)


    def test_get_user_no_authority(self):
        response = self.client.get(
            '/api/v1/user/me/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_(self):
        response = self.client.get(
            '/api/v1/user/me/',
            content_type='application/json',
            HTTP_AUTHORIZATION=self.inst1004_token
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["username"], "DJ")
        self.assertEqual(data["email"], "iteachwell@gmail.com")
        self.assertEqual(data["first_name"], "DJ")
        self.assertEqual(data["last_name"], "Lee")
        self.assertIn("last_login", data)
        self.assertIn("date_joined", data)
        self.assertNotIn("token", data)

        instructor = data["instructor"]
        self.assertIsNotNone(instructor)
        self.assertIn("id", instructor)
        self.assertEqual(instructor["company"], "LG CNS")
        self.assertEqual(instructor["year"], 1)
        self.assertEqual(len(instructor["charge"]), 0)

        self.assertIsNone(data["participant"])