from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]