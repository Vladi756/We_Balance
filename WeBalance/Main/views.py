from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def dashboard(request):
 	return render(request, 'dashboard.html')

class login(LoginView):
	template_name = 'login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('dashboard')

def register(request):
	if request.method =='POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration was successful")
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
		return redirect('register')
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"form":form})
