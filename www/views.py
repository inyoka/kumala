from django.shortcuts import render
from www.models import UserProfile
from www.forms import UserForm, ProfileForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    title_dict = {'page_title':'Home Page','page_desc':'Chandra Kumala School'}
    return render(request, 'www/home.html', context = title_dict)

def about(request):
    title_dict = {'page_title':'About Us'}
    return render(request, 'www/about.html', context = title_dict)

def courses(request):
    title_dict = {'page_title':'Courses'}
    return render(request, 'www/courses.html', context = title_dict)

def registration(request):
    title_dict = {'page_title':'Register'}
    return render(request, 'www/registration.html', context = title_dict)

def gallery(request):
    title_dict = {'page_title':'Gallery'}
    return render(request, 'www/gallery.html', context = title_dict)

def videos(request):
    title_dict = {'page_title':'Videos'}
    return render(request, 'www/videos.html', context = title_dict)

def contact(request):
    title_dict = {'page_title':'Contact Us'}
    return render(request, 'www/contact.html', context = title_dict)

def alumni(request):
    title_dict = {'page_title':'Alumni'}
    return render(request, 'www/alumni.html', context = title_dict)

def careers(request):
    title_dict = {'page_title':'Join Our Team'}
    return render(request, 'www/careers.html', context = title_dict)

def event(request):
    title_dict = {'page_title':'Trolls Performance','page_desc':'Chandra Kumala Primary School performance...'}
    return render(request, 'www/event.html', context = title_dict)

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
