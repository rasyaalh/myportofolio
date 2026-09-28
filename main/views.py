from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
import datetime

from main.models import Experience, Achievement, Education, Certification
from .forms import AchievementForm, ExperienceForm, EducationForm, CertificationForm

from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.core.exceptions import PermissionDenied

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# FUNGSI AUTENTIKASI (REGISTER, LOGIN, LOGOUT)
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat! Silakan login.')
            return redirect('main:login')
    
    context = {'form': form, 'name': 'Rasya Al Hawari'}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            return response
    else:
        form = AuthenticationForm(request)
        
    context = {'form': form, 'name': 'Rasya Al Hawari'}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

# FUNGSI MENAMPILKAN HALAMAN UTAMA (PUBLIK)
def show_main(request):
    if request.user.is_authenticated:
        if not Education.objects.filter(user=request.user).exists():
            Education.objects.create(user=request.user, institution="Universitas Indonesia", degree="Bachelor's Degree in Computer Science", period="2025 - Present")
            Education.objects.create(user=request.user, institution="MAN 1 Banda Aceh", degree="High School Education", period="2022 - 2025")
            Education.objects.create(user=request.user, institution="MTsN 1 Banda Aceh", degree="Junior High School Education", period="2019 - 2022")
            Education.objects.create(user=request.user, institution="SDN 22 Banda Aceh", degree="Elementary School Education", period="2013 - 2019")

        if not Achievement.objects.filter(user=request.user).exists():
            Achievement.objects.create(user=request.user, title="National Science Olympiad (OSN-K) - Informatics", rank="1st Place", description="Won 1st place in the 2024 Regency/City level...", year=2024)
            Achievement.objects.create(user=request.user, title="National Science Olympiad (OSN-P) - Informatics", rank="2nd Place", description="Secured 2nd place across Aceh...", year=2024)
            Achievement.objects.create(user=request.user, title="COINS INFEST X USK", rank="1st Place", description="Won 1st place in the Computer Olympiad of INFEST 2024.", year=2024)
            Achievement.objects.create(user=request.user, title="Computer Multi-Challenge Day USK", rank="2nd Place", description="Secured 2nd place in the Computer Olympiad competition at USK in 2024.", year=2024)
            Achievement.objects.create(user=request.user, title="National Insight Quiz Competition", rank="1st Place", description="Won 1st place with my team...", year=2024)
            Achievement.objects.create(user=request.user, title="MYRES 2023 (Top 30 National)", rank="National Semifinalist", description="Advanced to the semifinals...", year=2023)
            Achievement.objects.create(user=request.user, title="National Science Olympiad 2023 - Informatics", rank="3rd Place", description="Secured 3rd place in the city-level...", year=2023)

        if not Certification.objects.filter(user=request.user).exists():
            Certification.objects.create(user=request.user, title="Art & Design Fundamentals (10-Hour MOOC)", issuer="MPKT Final Project", issue_date=datetime.date(2026, 5, 10))

        if Experience.objects.filter(user=request.user).count() <= 1:
            Experience.objects.get_or_create(user=request.user, title="Class President, Olympiad Class", defaults={"description": "Led the Olympiad Class...", "category": "volunteer", "ended_at": timezone.now()})
            Experience.objects.get_or_create(user=request.user, title="Event Division Committee for Saleum 8", defaults={"description": "Managed and organized...", "category": "volunteer", "ended_at": timezone.now()})
            Experience.objects.get_or_create(user=request.user, title="Table Tennis Club Manager", defaults={"description": "Managed the school-level...", "category": "volunteer", "ended_at": timezone.now()})
            Experience.objects.get_or_create(user=request.user, title="Scout Leader", defaults={"description": "Participated in scouting...", "category": "volunteer", "ended_at": timezone.now()})
            Experience.objects.get_or_create(user=request.user, title="Project Officer, Saman Saweu Gampong (SSG)", defaults={"description": "Led the proposal drafting...", "category": "full-time", "ended_at": timezone.now()})
    
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    
    context = {
        "name": request.user.username if request.user.is_authenticated else "Rasya Al Hawari", 
        "npm": "2506534176",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia (Class of 2025) "
            "with a proven track record in informatics olympiads and academic research. "
            "Driven by a strong analytical mindset and a visionary approach to leadership."
        ),
        "last_login": last_login, 
    }
    return render(request, "index.html", context)

# FUNGSI MENAMPILKAN HALAMAN LIST (PUBLIK)
def show_experience(request):
    context = {
        "name": request.user.username if request.user.is_authenticated else "Rasya Al Hawari",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_achievements(request):
    context = {
        "name": request.user.username if request.user.is_authenticated else "Rasya Al Hawari",
        "achievement_list": Achievement.objects.all(),
    }
    return render(request, "achievements.html", context)

def show_education(request):
    context = {
        "name": request.user.username if request.user.is_authenticated else "Rasya Al Hawari",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def show_certifications(request):
    context = {
        "name": request.user.username if request.user.is_authenticated else "Rasya Al Hawari",
        "certification_list": Certification.objects.all(),
    }
    return render(request, "certifications.html", context)

# FUNGSI MEMBUAT DATA BARU (DIKUNCI: HANYA SUPERUSER)
@login_required(login_url='/login/')
def create_achievement(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = AchievementForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        achievement = form.save(commit=False)
        achievement.user = request.user
        achievement.save()
        messages.success(request, "Penghargaan baru berhasil ditambahkan!")
        return redirect("main:show_achievements")

    context = {"name": request.user.username, "form": form}
    return render(request, "achievement_form.html", context)

@login_required(login_url='/login/')
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        experience = form.save(commit=False)
        experience.user = request.user
        experience.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {"name": request.user.username, "form": form}
    return render(request, "experience_form.html", context)

@login_required(login_url='/login/')
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        education = form.save(commit=False)
        education.user = request.user
        education.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {"name": request.user.username, "form": form}
    return render(request, "education_form.html", context)

@login_required(login_url='/login/')
def create_certification(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = CertificationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        certification = form.save(commit=False)
        certification.user = request.user
        certification.save()
        messages.success(request, "Sertifikasi baru berhasil ditambahkan!")
        return redirect("main:show_certifications")

    context = {"name": request.user.username, "form": form}
    return render(request, "certification_form.html", context)

# FUNGSI DATA DELIVERY JSON (PUBLIK)
def get_achievements_json(request):
    data = Achievement.objects.all()
    return HttpResponse(serializers.serialize("json", data, use_natural_foreign_keys=True), content_type="application/json")

def get_experience_json(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data, use_natural_foreign_keys=True), content_type="application/json")

def get_education_json(request):
    data = Education.objects.all()
    return HttpResponse(serializers.serialize("json", data, use_natural_foreign_keys=True), content_type="application/json")

def get_certifications_json(request):
    data = Certification.objects.all()
    return HttpResponse(serializers.serialize("json", data, use_natural_foreign_keys=True), content_type="application/json")

# FUNGSI HAPUS & UBAH DATA (DIKUNCI: HANYA SUPERUSER)
@login_required(login_url='/login/')
def delete_achievement(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    data = get_object_or_404(Achievement, pk=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Penghargaan berhasil dihapus!")
    return redirect("main:show_achievements")

@login_required(login_url='/login/')
def delete_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    data = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
    return redirect("main:show_experience")

@login_required(login_url='/login/')
def delete_education(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    data = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
    return redirect("main:show_education")

@login_required(login_url='/login/')
def delete_certification(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    data = get_object_or_404(Certification, pk=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Sertifikasi berhasil dihapus!")
    return redirect("main:show_certifications")

@login_required(login_url='/login/')
def edit_achievement(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    data = get_object_or_404(Achievement, pk=id)
    form = AchievementForm(request.POST or None, instance=data)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Penghargaan berhasil diperbarui!")
        return redirect("main:show_achievements")
    
    context = {"name": request.user.username, "form": form}
    return render(request, "edit_achievement.html", context)

@login_required(login_url='/login/')
def edit_experience(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    data = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=data)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")
    
    context = {"name": request.user.username, "form": form}
    return render(request, "edit_experience.html", context)

@login_required(login_url='/login/')
def edit_education(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    data = get_object_or_404(Education, pk=id)
    form = EducationForm(request.POST or None, instance=data)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan berhasil diperbarui!")
        return redirect("main:show_education")
    
    context = {"name": request.user.username, "form": form}
    return render(request, "edit_education.html", context)

@login_required(login_url='/login/')
def edit_certification(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    data = get_object_or_404(Certification, pk=id)
    form = CertificationForm(request.POST or None, instance=data)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Sertifikasi berhasil diperbarui!")
        return redirect("main:show_certifications")
    
    context = {"name": request.user.username, "form": form}
    return render(request, "edit_certification.html", context)

# FUNGSI INTERAKSI (STAR) - BISA DIAKSES SEMUA USER YANG LOGIN
@login_required(login_url="/login/")
def toggle_star(request, id):
    # Mengambil data experience berdasarkan id
    experience = get_object_or_404(Experience, pk=id)
    
    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya
        # Kalau belum, tambahkan star
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
            
    return redirect("main:show_experience")