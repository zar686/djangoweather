from django.shortcuts import render

# Create your views here.

# basic python funciton passing home as a request to server, tell where to point
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})
