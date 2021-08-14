from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username











# class User(models.Model):
#     FirstName = models.CharField(max_length=200)
#     LastName = models.CharField(max_length=200)
#     Email = models.EmailField(max_length=254)
#
#     def __str__(self):
#         return self.FirstName + " " + self.LastName

# class UserFormModel(models.Model):
#     FirstName = models.CharField(max_length = 200)
#     LastName = models.CharField(max_length=200)
#     Email = models.EmailField(max_length=254)
#
#     # class Meta:
#     #     ordering = ['name']
#
#     def __str__(self):
#         return f"Form by {self.name}"
