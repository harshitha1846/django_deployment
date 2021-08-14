from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Your account is not active")

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'AppTwo/login.html')

def help(request):
    dic = {
    'content':"help page"
    }
    return render(request,'AppTwo/help.html',dic)

def image(request):
    return render(request,'static_image.html')

def users(request):
    users = User.objects.all()
    # users = User.objects.all()
    # users = {i.objects.values() for i in users}
    # print(users)
    # serial_no = [i for i in range(1,len(users)+1)]
    return render(request, 'AppTwo/user.html',context={'users':users})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit = False)

            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')

                profile.profile_pic = request.FILES['profile_pic']

                profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm(request.GET)
        profile_form = UserProfileForm(request.GET)

    return render(request,'AppTwo/register.html',
                        {'user_form':user_form,
                        'profile_form':profile_form,
                        'registered':registered
                        })















# def userform(request):
#     form = Form(request.GET)
#     if request.method == 'POST':
#         form = Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Your details has been stored')

    # else:
    #     form = Form(request.GET)
    #     context = {
    #         'form':form,
    #     }
    # # # form = forms.userForm(request.POST)
    # return render(request, 'AppTwo/form_page.html',{'form':form})
