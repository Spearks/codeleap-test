from django.test import TestCase
from rest_framework.test import APIClient
from api.models import Careers
class APICase(TestCase): 
    def setUp(self):
        self.client = APIClient()
        
        self.test_object = Careers.objects.create(
            username='jonny_doe',
            title='Lorem',
            content='lorem ipsum dolor sit amet',
        )        
    