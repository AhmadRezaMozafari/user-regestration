from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='log-in')
def indexPage(request):
    profile = request.user.profile
    return render(request,'index.html',context={'profile':profile})


def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username dose not exist!!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'You are logged in!')
            return redirect('index')
        else:
            messages.error(request, 'username or password is incorrect')

    return render(request, 'form.html')



def register_user(request):
    page = 'register'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={'page':page,'form':form}
    return render(request,'form.html',context)


def logOut(request):
    logout(request)
    return redirect('log-in')