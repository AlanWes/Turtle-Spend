from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from login_register_app.models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def MasterPage(request):
    return render (request,'master.html')

def RegisterPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        c_password=request.POST.get('confirm_password')
        money=request.POST.get('money')
        # Validation
        if password==c_password:
            if len(password) < 8:
                return render(request, 'register.html', {'error_message': 'Password must contain at least 8 characters.'})
            elif not any(char.isdigit() for char in password):
                return render(request, 'register.html', {'error_message': 'Password must contain at least one number.'})
            elif not any(char.isupper() for char in password):
                return render(request, 'register.html', {'error_message': 'Password must contain at least one uppercase character.'})
            else:
                try:
                    money = float(money)
                except ValueError:
                    return render(request, 'register.html', {'error_message': 'Invalid money value.'})
                user = User.objects.create_user(username=uname, email=email, password=password)
                profile = Profile.objects.create(user=user, money=money)
                return redirect('login')
        else:
            return render(request, 'register.html', {'error_message': "Those passwords didn't match. Try again."})

    return render (request,'register.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('login_pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Username or Password is incorrect.'})
       
    return render (request,'login.html')

@login_required(login_url='login')
def HomePage(request):
    user_profile = Profile.objects.get(user=request.user)
    money = user_profile.money

    return render(request, 'home.html', {'money': money})

def LogoutPage(request):
    logout(request)
    return redirect('master')
