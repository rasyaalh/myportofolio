from django.shortcuts import render
from main.models import Experience

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