from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProfileModel, CommentModel

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'
