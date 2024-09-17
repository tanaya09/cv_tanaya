from django.shortcuts import render
from .models import ContactInfo, Education, Skill, Experience, Project

def cv_view(request):
    contact_info = ContactInfo.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()

    context = {
        'contact_info': contact_info,
        'education': education,
        'skills': skills,
        'experiences': experiences,
        'Project': projects,
    }
    return render(request, 'cv/cv.html', context)
