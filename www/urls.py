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
from www.views import (Home, About, Programs, Registration, Gallery, Videos,
                    Contact, Alumni, Careers, Event, signup, user_login, Exams,
                    Parents, Reading, Scholarships, Trolls, Enroll, Space, News,
                    Awards, Splash, Options, Calendar)

# Template Tagging

app_name = 'www'

urlpatterns=[
    path('www/', Home.as_view(), name='www'),
    path('about', About.as_view(), name='about'),
    path('calendar', Calendar.as_view(), name='calendar'),
    path('news', News.as_view(), name='news'),
    path('exams', Exams.as_view(), name='exams'),
    path('options', Options.as_view(), name='options'),
    path('programs', Programs.as_view(), name='programs'),
    path('splash', Splash.as_view(), name='splash'),
    path('space', Space.as_view(), name='space'),
    path('scholarships', Scholarships.as_view(), name='scholarships'),
    path('register', Registration.as_view(), name='registration'),
    path('gallery', Gallery.as_view(), name='gallery'),
    path('trolls', Trolls.as_view(), name='trolls'),
    path('contact', Contact.as_view(), name='contact'),
    path('videos', Videos.as_view(), name='videos'),
    path('alumni', Alumni.as_view(), name='alumni'),
    path('awards', Awards.as_view(), name='awards'),
    path('careers', Careers.as_view(), name='careers'),
    path('event', Event.as_view(), name='event'),
    path('reading', Reading.as_view(), name='reading'),
    path('parents', Parents.as_view(), name='parents'),
    path('enroll', Enroll.as_view(), name='enroll'),
    path('signup', signup, name='signup'),
    path('user_login/', user_login, name='user_login'),
]
