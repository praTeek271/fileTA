from rest_framework import serializers
from .models import File
from django.contrib.auth.models import User

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['user', 'file', 'download_link']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']