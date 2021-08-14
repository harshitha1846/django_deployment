from django.urls import path
from . import views
app_name = 'AppTwo'
urlpatterns = [
    path('users/',views.users,name='users'),
    path('register/',views.register,name='register'),
    path('help/',views.help, name='help'),
    path('user_login/',views.user_login, name='user_login')
]
