from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def details(request):
    return render(request, 'portfolio-details.html')

def services(request):
    return render(request, 'service-details.html')

def base(request):
    return render(request, 'base.html')