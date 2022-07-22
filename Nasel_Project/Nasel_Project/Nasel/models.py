from django.db import models
from django.contrib.auth.models import User
# Create your models here

class ProfileModel (models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class CommentModel (models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Order (models.Model):


class Animal (models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    photo = models.URLField()
    father = models.CharField(max_length=200)
    mother = models.CharField(max_length=200)
    family= models.CharField(max_length=200)


