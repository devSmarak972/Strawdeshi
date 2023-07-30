from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
	

# Create your views here.
def home(request):
	return render(request,"home.html",{})
def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def register(request):
	if request.method == "POST":
		print(request.POST,request)
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			print("valid")
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("")
		print(form.errors)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CustomUserCreationForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def home2(request):
	return render(request,"index2.html",{})
def card(request):
	return render(request,"card.html",{})