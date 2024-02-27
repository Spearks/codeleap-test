from django.urls import path, include
from rest_framework import routers

from api.views import CareersViewSet

router = routers.DefaultRouter()
router.register('careers', CareersViewSet, 'careers')

urlpatterns = [
    path('', include(router.urls)),
]