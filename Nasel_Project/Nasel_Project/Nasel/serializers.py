from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProfileModel, CommentModel,AnimalModel,OrderModel

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'

class ProfileSerializerView(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = '__all__'

class AnimalSerializerView(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'

class OrderSerializerView(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
