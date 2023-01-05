from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Flagged, Preferences, WorkDone

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import PreferencesSerializer, WorkDoneSerializer, FlaggedSerializer
from django.http import JsonResponse
from rest_framework.response import Response

from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

@login_required(login_url="/login/")
def dashboard(request):
 	return render(request, 'dashboard.html')

@login_required(login_url="/login/")
def dashboard2(request):
 	return render(request, 'dashboard2.html')

@login_required(login_url="/login/")
def preferences(request):
	return render(request, 'preferences.html')

@login_required(login_url="/login/")
def report(request):
	return render(request, 'report.html')

@login_required(login_url="/login/")
def workMetrics(request):
	return render(request, 'workMetrics.html')

def terms_and_conditions(request):
	return render(request, 'terms_and_conditions.html')

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

@api_view(['POST'])
def addPreferences(request):
	serializer = PreferencesSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def addWorkDone(request):
	serializer = WorkDoneSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def flagUser(request):
	serializer = FlaggedSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET'])
def flaggedList(request):
	context_object_name = 'flagged'
	flagged = Flagged.objects.all()

	serializer = FlaggedSerializer(flagged, many=True)
	return Response(serializer.data)

class UserPreferences(APIView):
	context_object_name = 'preferences'

	def get(self, request, **kwargs):
		preferences = Preferences.objects.filter(user=self.request.user)

		serializer = PreferencesSerializer(preferences, many=True)
		return Response(serializer.data)

class takeActionOnFlag(UpdateView):
	model = Flagged
	fields = ['action_taken']
	template_name = 'update_form.html'
	success_url = reverse_lazy('report')

	def form_valid(self, form):
		return super(takeActionOnFlag, self).form_valid(form)

class getWorkDone(APIView):
	context_object_name = 'workdone'

	def get(self, request, **kwargs):
		workdone = WorkDone.objects.filter(user=self.request.user)

		serializer = WorkDoneSerializer(workdone, many=True)
		return Response(serializer.data)