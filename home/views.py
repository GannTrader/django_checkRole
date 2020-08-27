from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister, UserLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .decorators import checkRole
# Create your views here.
def registerUser(request):
	Form = UserRegister
	return render(request, 'home/register.html', {'form': Form})

def loginUser(request):
	Form = UserLogin
	return render(request, 'home/login.html', {'form': Form})

def getRegister(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']

	user = User.objects.create_user(username, email, password)
	user.save()
	return HttpResponse('success')


def getLogin(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponse('login success')
	else:
		return HttpResponse('login fail')

@login_required(login_url='/home/login/')
@checkRole(allowed_roles = ['Level 1'])
def level1(request):
	return render(request, 'home/level1.html')

@login_required(login_url='/home/login/')
@checkRole(allowed_roles = ['Level 2'])
def level2(request):
	return render(request, 'home/level2.html')