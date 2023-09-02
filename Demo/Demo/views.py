from django.http import HttpResponse
from django.shortcuts import render
#defining functions to be propmpted when url are called .

def about(request):
    #return HttpResponse('about')
    context = {
        'page_title': 'Home',
        'user_name': 'John',
    }
    return render(request,'about.html')

def homepage(request):
    #return HttpResponse('Home Page')
    return render(request,'homepage.html')

