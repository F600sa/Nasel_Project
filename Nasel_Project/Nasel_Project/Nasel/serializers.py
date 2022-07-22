from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProfileModel, CommentModel,Animal

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'

class AnimapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
