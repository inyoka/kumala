from django.shortcuts import render

# Create your views here.

def www(request):
    my_dict = {'insert_content':'HELLO I AM FROM FIRST APP!!!!'}
    return render(request, 'www/index.html', context = my_dict)
