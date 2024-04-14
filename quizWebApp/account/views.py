from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile

# Create your views here.

def register(request):

    if request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            # check for same emails
            if User.objects.filter(email=email).exists():
                messages.info(request, "E-mail already used. Try to Login")
                return redirect('register')

            # check for same users
            elif User.objects.filter(username=username).exists():
                messages.info(request, "UserName already taken")
                return redirect('register')
            
            else:
                # create user
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # log user and show profile
                user_login=auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create profile new user
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model, email_address=email)
                new_profile.save()
                return redirect('profile', user_model.username)
        else:
            messages.info(request, "Password not Matching!")
            return redirect('register')


    context={}
    return render(request, 'register.html', context)


def profile(request, username):

    user_object=User.objects.get(username=username)
    user_profile=Profile.objects.get(user=user_object)


    context={"user_profile":user_profile}
    return render(request, "profile.html", context)


def login(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile', username)
        else:
            messages.info(request, 'Credentials Invalid!')
            return redirect('login')

    return render(request, "login.html")