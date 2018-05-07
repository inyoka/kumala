from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View, TemplateView

from www.models import UserProfile
from www.forms import UserForm, ProfileForm

class Home(TemplateView):
    template_name = 'www/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Home Page'
        context['page_desc'] = 'Chandra Kumala School'
        return context

class About(TemplateView):
    template_name = 'www/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'About Us'
        return context

class Exams(TemplateView):
    template_name = 'www/exams.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Exam Timetable'
        return context

class Programs(TemplateView):
    template_name = 'www/programs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Programs'
        return context

class Enroll(TemplateView):
    template_name = 'www/enroll.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Enroll @CKS'
        context['page_desc'] = 'Please fill in this preliminary application form so that we can check availability for your child.'
        return context


class Scholarships(TemplateView):
    template_name = 'www/scholarships.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Scholarships'
        return context

class Registration(TemplateView):
    template_name = 'www/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Register'
        return context

class Gallery(TemplateView):
    template_name = 'www/media/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Gallery'
        return context

class Trolls(TemplateView):
    template_name = 'www/media/trolls.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Trolls'
        return context
class Videos(TemplateView):
    template_name = 'www/media/videos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Videos'
        return context


class Contact(TemplateView):
    template_name = 'www/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Contact'
        return context


class Alumni(TemplateView):
    template_name = 'www/alumni.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Alumni'
        return context


class Careers(TemplateView):
    template_name = 'www/careers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Careers'
        return context

class Workshop(TemplateView):
    template_name = 'www/workshop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Parents Enrichment Program'
        context['page_desc'] = 'Support and training for students parents.'
        return context

class Reading(TemplateView):
    template_name = 'www/reading.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Reading Workshop'
        context['page_desc'] = 'Support and training to help encourage student reading.'
        return context

class Event(TemplateView):
    template_name = 'www/event.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Event'
        return context

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    title_dict = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered, 'page_title':'Sign-up','page_desc':'Create an account'}
    return render(request, 'www/signup.html', context = title_dict,)

    # title_dict = {'page_title':'Sign-up','page_desc':'Create an account'}
    # return render(request, 'www/signup.html', context = title_dict)


def user_login(request):

    if request.method == 'POST':
        _username = request.POST.get('username')
        _password = request.POST.get('password')

        user = authenticate(username=_username, password=_password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active, contact administrator.")
        else:
            print("Someone tried to login and failed!")
            print(f"Username: {_username} and password {_password}")
            return HttpResponse("invalid login details supplied!")
    else:
        title_dict = {'page_title':'Login','page_desc':'Please enter username and password.'}
        return render(request, 'www/login.html', context = title_dict)
