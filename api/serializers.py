from api.models import Careers
from accounts.models import User

from rest_framework import serializers

class CareersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    class Meta:
        model = Careers
        fields = ["id", "username", "created_datetime", "title", "content"]

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("User does not exist")
        return value

    def create(self, validated_data):
        username = validated_data.pop('user')['username']
        user = User.objects.get(username=username)
        return Careers.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        username = validated_data.pop('user', {}).get('username')
        if username is not None:
            user = User.objects.get(username=username)
            instance.user = user
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance