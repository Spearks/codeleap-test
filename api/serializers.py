from api.models import Careers
from rest_framework import serializers

class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'