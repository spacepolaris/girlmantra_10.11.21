"""girlmantra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webappgm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapi/', views.test_api.as_view()),
    path('testapiupdate/', views.test_update_api.as_view()),
    # Registration API
    path('startonboarding/', views.start_onboard_post_api.as_view()),
    path('savepersonalinfo/', views.save_personal_info_post_api.as_view()),
    path('savegoals/', views.save_goals_post_api.as_view()),
    path('saveproblems/', views.save_problems_post_api.as_view()),
    path('savepreferredtime/', views.save_preferred_time_post_api.as_view()),
    path('getuserfullstatus/', views.get_user_full_status_api.as_view()),
    path('getuserregistrationstatus/', views.get_user_registration_status_api.as_view()),
    path('getpersonalinfo/', views.get_personal_info_api.as_view()),
    path('getgoals/', views.get_goals_api.as_view()),
    path('getproblems/', views.get_problems_api.as_view()),
    path('getpreferredtime/', views.get_preferred_time_api.as_view()),
]
