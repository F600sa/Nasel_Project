from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProfileModel, CommentModel

class ProfileSerializer(serializers.ModelSerializer):
    class meta:
        model = ProfileModel
        fields = '__all__'

