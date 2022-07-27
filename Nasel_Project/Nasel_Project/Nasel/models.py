from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your models here




class CommentModel (models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class AnimalModel (models.Model):
    photo = models.URLField(blank=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.IntegerField(blank=True)
    father = models.CharField(max_length=200)
    mother = models.CharField(max_length=200)
    family= models.CharField(max_length=200)
    awards = models.CharField(max_length=200,blank=True)
    award1 = models.CharField(max_length=200,blank=True)
    award2 = models.CharField(max_length=200,blank=True)
    award3 = models.CharField(max_length=200,blank=True)
    price=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProfileModel (models.Model):
    name = models.CharField(max_length=200)
    # image = models.URLField(blank=False)
    # bio = models.CharField(max_length=200,blank=True)
    phone=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    Street=models.CharField(max_length=200)
    animal = models.ForeignKey(AnimalModel,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class OrderModel (models.Model):
    # Choices=(
    #     ('نعم احتاج الى شركة توصيل','نعم احتاج الى شركة توصيل')
    #     ,('سوف استلم الطلب بنفسي ','سوف استلم الطلب بنفسي ')
    # )
    city=models.CharField(max_length=200)
    # delivery=models.CharField(max_length=50,choices=Choices)
    # Animal = models.ForeignKey(AnimalModel, on_delete=models.CASCADE)
    price=models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    iban=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)


class Review (models.Model):
    rating = models.DecimalField(max_digits = 3 ,decimal_places = 1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)





