from django.shortcuts import render
from django.utils import timezone
import datetime
from main.models import Experience, Achievement, Education, Certification

def show_main(request):
    # SKRIP AUTO-POPULATE DATABASE PWS
    if not Education.objects.exists():
        Education.objects.create(institution="Universitas Indonesia", degree="Bachelor's Degree in Computer Science", period="2025 - Present")
        Education.objects.create(institution="MAN 1 Banda Aceh", degree="High School Education", period="2022 - 2025")
        Education.objects.create(institution="MTsN 1 Banda Aceh", degree="Junior High School Education", period="2019 - 2022")
        Education.objects.create(institution="SDN 22 Banda Aceh", degree="Elementary School Education", period="2013 - 2019")

    if not Achievement.objects.exists():
        Achievement.objects.create(title="National Science Olympiad (OSN-K) - Informatics", rank="1st Place", description="Won 1st place in the 2024 Regency/City level National Science Olympiad in Informatics, advancing to the provincial level.", year=2024)
        Achievement.objects.create(title="National Science Olympiad (OSN-P) - Informatics", rank="2nd Place", description="Secured 2nd place across Aceh in the 2024 Provincial level National Science Olympiad in Informatics.", year=2024)
        Achievement.objects.create(title="COINS INFEST X USK", rank="1st Place", description="Won 1st place in the Computer Olympiad of INFEST 2024.", year=2024)
        Achievement.objects.create(title="Computer Multi-Challenge Day USK", rank="2nd Place", description="Secured 2nd place in the Computer Olympiad competition at USK in 2024.", year=2024)
        Achievement.objects.create(title="National Insight Quiz Competition", rank="1st Place", description="Won 1st place with my team in the National Insight Quiz Competition held at SMA Methodist Banda Aceh in 2024.", year=2024)
        Achievement.objects.create(title="MYRES 2023 (Top 30 National)", rank="National Semifinalist", description="Advanced to the semifinals in the MST field with the research paper: 'Analysis of Facial Expressions of Autistic Children in Non-Verbal Communication through Thermal Imaging Technology'.", year=2023)
        Achievement.objects.create(title="National Science Olympiad 2023 - Informatics", rank="3rd Place", description="Secured 3rd place in the city-level (Banda Aceh) OSN 2023 and advanced to the provincial level as a finalist.", year=2023)

    if not Certification.objects.exists():
        Certification.objects.create(title="Art & Design Fundamentals (10-Hour MOOC)", issuer="MPKT Final Project", issue_date=datetime.date(2026, 5, 10))

    if not Experience.objects.exists():
        Experience.objects.create(title="Project Officer, Saman Saweu Gampong (SSG)", description="Led the proposal drafting, managed data organization, and served as the Project Officer for the SSG 2026 cultural performance outreach.", category="full-time", ended_at=timezone.now())
    # -

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