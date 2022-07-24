from django.db import models
from django.contrib.auth.models import User
# Create your models here




class CommentModel (models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class AnimalModel (models.Model):
    photo = models.URLField()
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    father = models.CharField(max_length=200)
    mother = models.CharField(max_length=200)
    family= models.CharField(max_length=200)
    awards = models.CharField(max_length=200)
    price=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class ProfileModel (models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    animal = models.ForeignKey(AnimalModel,on_delete=models.CASCADE)

class OrderModel (models.Model):
    Animal = models.ForeignKey(AnimalModel, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    profile = models.ForeignKey(ProfileModel, on_delete=models.DO_NOTHING)


class Review (models.Model):
    rating = models.DecimalField(max_digits = 3 ,decimal_places = 1)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)



