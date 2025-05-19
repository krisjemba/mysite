from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index/home.html')

def collaborate(request):
    return render(request, 'index/collaborate.html')

def communities(request):
    return render(request, 'index/communities.html')

def connect(request):
    return render(request, 'index/connect.html')

def blog(request):
    return render(request, 'index/blog.html')