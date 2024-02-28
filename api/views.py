# Create your views here.

# Views for the App
from .models import Careers
from rest_framework import permissions, viewsets

from api.serializers import CareersSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
#Permission that allows users to create posts only with their username
class UsernamePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return obj.user.username == request.user.username

# Crud for careers
class CareersViewSet(viewsets.ModelViewSet):
    """
    CRUD API v1.0 endpoint for careers
    """
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, UsernamePermission)
 
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)