from django.shortcuts import render
from main.models import Experience, Achievement, Education, Certification

def show_main(request):
    context = {
        "name": "Rasya Al Hawari",
        "npm": "2506534176",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia (Class of 2025) "
            "with a proven track record in informatics olympiads and academic research. "
            "Driven by a strong analytical mindset and a visionary approach to leadership."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Rasya Al Hawari",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

#TUGAS 2

def show_achievements(request):
    context = {
        "name": "Rasya Al Hawari",
        "achievement_list": Achievement.objects.all(),
    }
    return render(request, "achievements.html", context)

def show_education(request):
    context = {
        "name": "Rasya Al Hawari",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_certifications(request):
    context = {
        "name": "Rasya Al Hawari",
        "certification_list": Certification.objects.all(),
    }
    return render(request, "certifications.html", context)