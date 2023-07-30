from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
	

import git
# from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update(request):
	if request.method == "POST":
		'''
		pass the path of the diectory where your project will be 
		stored on PythonAnywhere in the git.Repo() as parameter.
		Here the name of my directory is "test.pythonanywhere.com"
		'''
		repo = git.Repo("../../") 
		origin = repo.remotes.origin

		origin.pull()
		# reload()
		return HttpResponse("Updated code on PythonAnywhere")
	
	else:
		return HttpResponse("Couldn't update the code on PythonAnywhere")

# Create your views here.
def home(request):
	return render(request,"home.html",{})
def login_user(request):
	if request.method == "POST":
		if "email" in request.POST and "password" in request.POST:
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user is not None:
					login(request, user)
					print("logged in")
					messages.info(request, f"You are now logged in as {user.first_name}.")
					return redirect("/")
			else:
					messages.error(request,"Invalid username or password.")
		
	return render(request=request, template_name="login.html", context={"messages":messages})
# def login_user(request):
#     logout(request)
#     username = password = ''
#     if request.POST:
		
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/main/')
#     return render_to_response('login.html', context_instance=RequestContext(request))

def register_user(request):
	if request.method == "POST":
		print(request.POST,request)
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			print("valid")
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		print(form.errors)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CustomUserCreationForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def home2(request):
	return render(request,"index2.html",{})
def card(request):
	return render(request,"card.html",{})