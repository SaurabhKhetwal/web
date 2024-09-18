"""
URL configuration for ci_projectfile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ci_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='home'),
    path('contact-us/', views.contactus),
    path('saveenquiry/', views.saveEnquiry, name='saveenquiry'),
    path('our-services/', views.Ourservices),
    path('about-us/', views.aboutus),
    path('web-development/', views.web_development_page),
    path('our-services/web-development/', views.web_development_page),
    path('app-development/', views.app_develpment_page),
    path('ux-ui/', views.ux_ui_page),
    path('digitalmarketing/', views.digitalmarketing),
    
    
]
