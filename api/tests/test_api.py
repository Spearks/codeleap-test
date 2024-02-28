from api.tests.test_setup import APICase
from api.models import Careers
from api.serializers import CareersSerializer

from rest_framework import status
from django.urls import reverse
import json

class CareersTest(APICase):
    
    def test_get_all_careers(self):
        url = reverse('careers-list')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 1)
    
        json_data = CareersSerializer(Careers.objects.all(), many=True).data
        
        self.assertEqual(response.data, json_data)
    
    def test_post_career(self):
        url = reverse('careers-list')
        
        data = {
            'username' : self.user.username,
            'title' : 'Lorem2',
            'content' : 'lorem ipsum dolor sit amet2'
        }
        
        response = self.client.post(content_type='application/json', path=url, data=json.dumps(data))
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(Careers.objects.all().last().user.username, data['username'])
        self.assertEqual(Careers.objects.all().last().title, data['title'])
        self.assertEqual(Careers.objects.all().last().content, data['content'])

    def test_update_career(self):
        url = reverse('careers-detail', args=[self.test_object.id])

        data = {
            'username' : self.user.username,
            'title' : 'I was changed!',
            'content' : 'Im also changed!'
        }
        
        response = self.client.patch(content_type='application/json', path=url, data=json.dumps(data))
        
        self.test_object.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.test_object.user.username, data['username'])
        self.assertEqual(self.test_object.title, data['title'])
        self.assertEqual(self.test_object.content, data['content'])
    
    def test_update_career_only_for_owner(self):
        # Change JWT for user self.second_user
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.second_jwt}')
        
        url = reverse('careers-detail', args=[self.test_object.id]) # This object is owned by self.user

        data = {
            'username' : self.second_user.username,
            'title' : 'I was changed!',
            'content' : 'Im also changed!'
        }
        
        response = self.client.patch(content_type='application/json', path=url, data=json.dumps(data))
        
        self.test_object.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.test_object.user.username, self.user.username)