# Create your views here.

# Views for the App
from .models import Careers
from rest_framework import permissions, viewsets

from api.serializers import CareersSerializer

# Crud for careers
class CareersViewSet(viewsets.ModelViewSet):
    """
    CRUD API v1.0 endpoint for careers
    """
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
 
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)