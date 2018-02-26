from django.shortcuts import render

# Create your views here.

def home(request):
    title_dict = {'page_title':'Home Page'}
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

def playday(request):
    title_dict = {'page_title':'Play Day','page_desc':'Creative hobbies and activities to release your inner child and supercharge your learning.'}
    return render(request, 'www/playday.html', context = title_dict)
