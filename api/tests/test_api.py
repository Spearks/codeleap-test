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
            'username' : 'jonny_doe2',
            'title' : 'Lorem2',
            'content' : 'lorem ipsum dolor sit amet2'
        }
        
        response = self.client.post(content_type='application/json', path=url, data=json.dumps(data))
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(Careers.objects.all().last().username, data['username'])
        self.assertEqual(Careers.objects.all().last().title, data['title'])
        self.assertEqual(Careers.objects.all().last().content, data['content'])

    def test_update_career(self):
        url = reverse('careers-detail', args=[self.test_object.id])

        data = {
            'username' : 'foobar',
            'title' : 'I was changed!',
            'content' : 'Im also changed!'
        }
        
        response = self.client.patch(content_type='application/json', path=url, data=json.dumps(data))
        
        self.test_object.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.test_object.username, data['username'])
        self.assertEqual(self.test_object.title, data['title'])
        self.assertEqual(self.test_object.content, data['content'])