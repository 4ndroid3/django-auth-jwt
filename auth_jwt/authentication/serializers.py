from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """ Serializador para manejar los usuarios """
    class Meta:
        model = User
        fields = '__all__'