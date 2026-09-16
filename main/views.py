from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
import datetime

from main.models import Experience, Achievement, Education, Certification
from .forms import AchievementForm, ExperienceForm, EducationForm, CertificationForm

from django.http import HttpResponse
from django.core import serializers

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

    if Experience.objects.count() <= 1:
        Experience.objects.get_or_create(title="Class President, Olympiad Class", defaults={"description": "Led the Olympiad Class at MAN 1 Banda Aceh. Implemented various improvements focused on class infrastructure and fostering better synergy among students.", "category": "volunteer", "ended_at": timezone.now()})
        Experience.objects.get_or_create(title="Event Division Committee for Saleum 8", defaults={"description": "Managed and organized the event division for the Saleum 8 activities held at MAN 1 Banda Aceh.", "category": "volunteer", "ended_at": timezone.now()})
        Experience.objects.get_or_create(title="Table Tennis Club Manager", defaults={"description": "Managed the school-level table tennis organization and coordinated its activities.", "category": "volunteer", "ended_at": timezone.now()})
        Experience.objects.get_or_create(title="Scout Leader", defaults={"description": "Participated in scouting activities, competed in city to provincial-level championships, and served as the Scout Leader for MTsN 1 Banda Aceh.", "category": "volunteer", "ended_at": timezone.now()})
        Experience.objects.get_or_create(title="Project Officer, Saman Saweu Gampong (SSG)", defaults={"description": "Led the proposal drafting, managed data organization, and served as the Project Officer for the SSG 2026 cultural performance outreach.", "category": "full-time", "ended_at": timezone.now()})
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

# FUNGSI MENAMPILKAN HALAMAN

def show_experience(request):
    context = {
        "name": "Rasya Al Hawari",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

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

# FUNGSI MEMBUAT DATA BARU (FORM POST)

def create_achievement(request):
    form = AchievementForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Penghargaan baru berhasil ditambahkan!")
        return redirect("main:show_achievements")

    context = {"name": "Rasya Al Hawari", "form": form}
    return render(request, "achievement_form.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {"name": "Rasya Al Hawari", "form": form}
    return render(request, "experience_form.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {"name": "Rasya Al Hawari", "form": form}
    return render(request, "education_form.html", context)

def create_certification(request):
    form = CertificationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Sertifikasi baru berhasil ditambahkan!")
        return redirect("main:show_certifications")

    context = {"name": "Rasya Al Hawari", "form": form}
    return render(request, "certification_form.html", context)

# FUNGSI DATA DELIVERY (JSON)
def get_achievements_json(request):
    data = Achievement.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_experience_json(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_education_json(request):
    data = Education.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_certifications_json(request):
    data = Certification.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# FUNGSI HAPUS DATA (DELETE)
def delete_achievement(request, id):
    data = get_object_or_404(Achievement, pk=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Penghargaan berhasil dihapus!")
    return redirect("main:show_achievements")

def delete_experience(request, id):
    data = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
    return redirect("main:show_experience")

def delete_education(request, id):
    data = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
    return redirect("main:show_education")

def delete_certification(request, id):
    data = get_object_or_404(Certification, pk=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Sertifikasi berhasil dihapus!")
    return redirect("main:show_certifications")