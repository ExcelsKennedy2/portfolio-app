from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    about = About.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    experience = Experience.objects.all()
    projects = Project.objects.all()
    service = Service.objects.all()
    contact = Contact.objects.all()
    link = Link.objects.all()
    testimonial = Testimonial.objects.all()

    context = {
        'about': about,
        'education': education,
        'skills': skills,
        'experience': experience,
        'projects': projects,
        'service': service,
        'contact': contact,
        'link': link,
        'testimonial': testimonial,
    }

    return render(request, 'index.html', context)

def details(request):
    return render(request, 'portfolio-details.html')

def services(request):
    return render(request, 'service-details.html')

def base(request):
    return render(request, 'base.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'index.html')