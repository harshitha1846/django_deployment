from .models import UserProfile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password') #['firstname', 'lastname', 'email']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)








# class Form(ModelForm):
#     # firstname = forms.CharField(label='')
#     # lastname = forms.CharField(label='')
#     # email = forms.EmailField(label='')
#
#     class Meta:
#         model = User
#         fields = '__all__' #['firstname', 'lastname', 'email']
#
#     # firstname = forms.CharField()
#     # lastname = forms.CharField()
#     # email = forms.EmailField()
