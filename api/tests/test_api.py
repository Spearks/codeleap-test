from api.tests.test_setup import APICase
from api.models import Careers
from api.serializers import CareersSerializer

class CareersTest(APICase):
    def setUp(self):
        Careers.objects.create(
            username='jonny_doe',
            title='Lorem',
            content='lorem ipsum dolor sit amet',
        )        
    
    def test_get_all_careers(self):
        response = self.client.get('/careers/')
        
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(len(response.data), 1)
    
        json_data = CareersSerializer(Careers.objects.all(), many=True).data
        
        self.assertEqual(response.data, json_data)