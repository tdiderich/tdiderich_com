from django.http import HttpResponse
from django.shortcuts import render

#home page
def home(request):
    return render(request, 'home.html')

#about page
def about(request):
    return render(request, 'about.html')

#contact page
def contact(request):
    return render(request, 'contact.html')        
