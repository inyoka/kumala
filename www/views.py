from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'www/home.html')

def about(request):
    return render(request, 'www/about.html')

def academics(request):
    return render(request, 'www/academics.html')

def admissions(request):
    return render(request, 'www/admissions.html')

def gallery(request):
    return render(request, 'www/gallery.html')

def relative(request):
    return render(request, 'www/relative_url_templates.html')
