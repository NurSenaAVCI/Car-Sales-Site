from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import User


def login_view(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = User.objects.get(email = email).username
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                messages.success(request, 'Login Succesfully!')
                return redirect('index_page')
            
            else:
                messages.warning(request, 'User not found')
                return render (request, 'user/login.html', {
                    'form' : form})
            
        else:
            return render (request, 'user/login.html', {
                'form' : form})

    else:
        form = UserLoginForm()
        return render (request, 'user/login.html', {
            'form' : form
        })

def signup_view(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                messages.success(request,'User created')
                return redirect('index_page')
        
            else:
                messages.error(request,'User creation failed')
                return render(request, 'user/signup.html', {
                    'form': form,
                })
            
        else:
            return render(request, 'user/signup.html', {'form': form, 'error': 'User creation failed'})
        
    form = SignUpForm()
    return render(request, 'user/signup.html', {
        'form': form
    })
    
def logout_view(request):
    logout(request)
    return redirect('index_page')

def profile_view(request):
    user = request.user
    
    profile = Profile.objects.filter(user=request.user).first()
    form = ProfileForm(instance=profile)
    
    user_form = UserInformationForm(initial={
        'email': user.email,
        'username': user.username,
    })

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']

            profile = Profile(user=user, name=name, city=city, phone=phone)
            profile.save()
            messages.success(request, "Profile save succesfully")

            return render(request, 'user/profile.html', {
                'form' : form,
                'user_form' : user_form,
            })

    return render(request, 'user/profile.html', {
        'form' : form,
        'user_form' : user_form,
    })

def password_change(request):

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            
            messages.info(request, 'Your Password Has Been Successfully Changed...')
            return redirect('index_page')
        else:
            messages.error(request, 'An error occurred, try again later.')
            return render(request, 'user/password.html', {
                'form': form
            })
            
    form = PasswordForm(request.user)
    return render(request, 'user/password.html', {
        'form': form
    })
