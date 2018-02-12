from django.shortcuts import render

# Create your views here.

def home(request):
    title_dict = {'page_title':'Home Page'}
    return render(request, 'www/home.html', context = title_dict)

def about(request):
    title_dict = {'page_title':'About our school'}
    return render(request, 'www/about.html', context = title_dict)

def academics(request):
    title_dict = {'page_title':'Academic Courses Offered'}
    return render(request, 'www/academics.html', context = title_dict)

def admissions(request):
    title_dict = {'page_title':'Admissions process'}
    return render(request, 'www/admissions.html', context = title_dict)

def gallery(request):
    title_dict = {'page_title':'Gallery'}
    return render(request, 'www/gallery.html', context = title_dict)

def contact(request):
    title_dict = {'page_title':'Contact Us'}
    return render(request, 'www/contact.html', context = title_dict)
