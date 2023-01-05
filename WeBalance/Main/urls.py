from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('preferences/', views.preferences, name='preferences'),
    path('report/', views.report, name='report'),
    path('workdone/', views.workMetrics, name='workdone'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('save-preferences/', views.addPreferences, name='add_preferences'),
    path('save-worklog/', views.addWorkDone, name='add_workdone'),
    path('dashboard/user/', views.dashboard2, name='dashboard2'),
    path('flag-user/', views.flagUser, name='flag_user'),
    path('flagged-list/', views.flaggedList, name='flagged_list'),
    path('user-preferences/', views.UserPreferences.as_view(), name='user_preferences'),
    path('edit-flag/<int:pk>/', views.takeActionOnFlag.as_view(), name='flag_edit'),
    path('user-workdone/', views.getWorkDone.as_view(), name='user_workdone'),
]