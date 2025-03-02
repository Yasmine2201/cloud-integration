from rest_framework import serializers

from core_models.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'username': {'required': False, 'allow_blank': True}}


