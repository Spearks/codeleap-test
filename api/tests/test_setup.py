from django.test import TestCase
from rest_framework.test import APIClient
from api.models import Careers
from accounts.models import User
from rest_framework_simplejwt.tokens import AccessToken
class APICase(TestCase): 
    def setUp(self):
        
        self.client = APIClient()
        
        self.user = User.objects.create(username="jonny_doe", email="jonny@example.com", password="PaSsWord!123")
        
        self.second_user = User.objects.create(username="foobar_doe", email="foobar@example.com", password="PaSsWord!123")
        
        self.test_object = Careers.objects.create(
            user=self.user,
            title='Lorem',
            content='lorem ipsum dolor sit amet',
        )
        
        self.token = AccessToken.for_user(self.user)
        
        self.second_token = AccessToken.for_user(self.second_user)
        
        jwt = str(self.token)
        
        self.second_jwt = str(self.second_token)
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {jwt}')

           
