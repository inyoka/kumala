"""kumala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from www.views import Home
from www.views import Home, About, Programs, Registration, Gallery, Videos
from www.views import Contact, Alumni, Careers, Event, signup, user_login

# Template Tagging

app_name = 'www'

urlpatterns=[
    path('www/', Home.as_view(), name='www'),
    path('about', About.as_view(), name='about'),
    path('programs', Programs.as_view(), name='programs'),
    path('register', Registration.as_view(), name='registration'),
    path('gallery', Gallery.as_view(), name='gallery'),
    path('contact', Contact.as_view(), name='contact'),
    path('videos', Videos.as_view(), name='videos'),
    path('alumni', Alumni.as_view(), name='alumni'),
    path('careers', Careers.as_view(), name='careers'),
    path('event', Event.as_view(), name='event'),
    path('signup', signup, name='signup'),
    path('user_login/', user_login, name='user_login'),
]
