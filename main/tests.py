from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Achievement, Education, Certification

class MainTest(TestCase):
    def setUp(self):
        # Setup data dummy untuk Experience
        self.experience = Experience.objects.create(
            title="Pengalaman Testing Sementara",
            description="Ini hanya deskripsi untuk menguji database.",
            category="volunteer",
        )
        
        # Setup data dummy untuk Achievement (Tugas 2)
        self.achievement = Achievement.objects.create(
            title="Juara 1 Lomba Testing",
            rank="1st Place",
            description="Menang lomba testing skala nasional.",
            year=2024
        )
        
        # Setup data dummy untuk Education (Tugas 2)
        self.education = Education.objects.create(
            institution="Universitas Testing Indonesia",
            degree="Sarjana Komputer",
            period="2025 - Present"
        )
        
        # Setup data dummy untuk Certification (Tugas 2)
        self.certification = Certification.objects.create(
            title="Sertifikat Ahli Testing",
            issuer="TestingCorp",
            issue_date=timezone.now().date()
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_achievements_url_and_data(self):
        response = self.client.get(reverse("main:show_achievements"))
        self.assertEqual(response.status_code, 200) # Cek URL dapat diakses
        self.assertTemplateUsed(response, "achievements.html") # Cek template benar
        self.assertContains(response, self.achievement.title) # Cek data muncul

    def test_empty_achievements_page(self):
        Achievement.objects.all().delete()
        response = self.client.get(reverse("main:show_achievements"))
        self.assertContains(response, "Belum ada prestasi yang ditambahkan.")

    def test_education_url_and_data(self):
        response = self.client.get(reverse("main:show_education"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.institution)

    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))
        self.assertContains(response, "Belum ada riwayat pendidikan yang ditambahkan.")

    def test_certifications_url_and_data(self):
        response = self.client.get(reverse("main:show_certifications"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certifications.html")
        self.assertContains(response, self.certification.title)

    def test_empty_certifications_page(self):
        Certification.objects.all().delete()
        response = self.client.get(reverse("main:show_certifications"))
        self.assertContains(response, "Belum ada sertifikasi yang ditambahkan.")