from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if not (username and email and password1 and password2):  # Check if any field is empty
            messages.error(request, 'Please fill in all the fields')
            return render(request, 'userauth/signup.html')
        
        if password1 != password2:
            messages.error(request, 'Please enter the same password')
            return render(request, 'userauth/signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username already exists')
            return render(request, 'userauth/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email already exists')
            return render(request, 'userauth/signup.html')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        auth.login(request, user)
        messages.success(request, 'Registration successful')
        user.save()
        return redirect('index')
    else:
        return render(request, 'userauth/signup.html')

def login(request):
    
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password1']
        user=auth.authenticate(email=email,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are succesfuly logged in')
            return redirect('index')
        else:
            messages.error(request,'invalid login credential')
            return redirect('login')
   

    return render(request,'userauth/login.html')


def logout_view(request):
    logout(request)
    return redirect('index') 