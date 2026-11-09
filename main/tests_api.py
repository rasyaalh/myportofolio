import uuid
from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from main.models import Experience, Achievement, Education, Certification

class MegaPortfolioAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(username="owner", password="test-password")
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        
        # Setup Data
        self.ach = Achievement.objects.create(title="Juara", rank="1", description="desc", year=2024, user=self.owner)
        self.edu = Education.objects.create(institution="UI", degree="S1", period="2025", user=self.owner)
        self.cert = Certification.objects.create(title="AWS", issuer="Amazon", issue_date="2025-01-01", user=self.owner)
        
        self.ach_url = reverse("api:achievement-list")
        self.edu_url = reverse("api:education-list")

    # 1. TEST CSRF (Syarat Wajib Tugas 6)
    def test_csrf_protection_on_write(self):
        csrf_client = APIClient(enforce_csrf_checks=True)
        csrf_client.login(username="owner", password="test-password")
        
        # POST tanpa X-CSRFToken harus ditolak (403)
        response = csrf_client.post(self.ach_url, {"title": "Test", "rank": "1", "description": "D", "year": 2025}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 2. TEST ROLE & PERMISSION (Tugas 6)
    def test_guest_cannot_write_any_model(self):
        self.client.force_authenticate(user=self.visitor)
        self.assertEqual(self.client.post(self.ach_url, {}, format="json").status_code, 403)
        self.assertEqual(self.client.post(self.edu_url, {}, format="json").status_code, 403)

    # 3. TEST VALIDASI XSS / KOSONG (Tugas 6)
    def test_validation_rejects_empty_html(self):
        self.client.force_authenticate(user=self.owner)
        res = self.client.post(self.edu_url, {"institution": "   ", "degree": "S1", "period": "2025"}, format="json")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("institution", res.data)

    # 4. TEST STAR (Tugas 6)
    def test_star_toggles(self):
        self.client.force_authenticate(user=self.visitor)
        url = reverse("api:education-star", args=[self.edu.id])
        
        # Tambah Star
        res1 = self.client.post(url)
        self.assertTrue(res1.data["is_starred"])
        self.assertEqual(res1.data["star_count"], 1)
        
        # Hapus Star
        res2 = self.client.post(url)
        self.assertFalse(res2.data["is_starred"])
        self.assertEqual(res2.data["star_count"], 0)