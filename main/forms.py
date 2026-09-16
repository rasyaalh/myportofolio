from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select, DateInput
from main.models import Achievement, Experience, Education, Certification

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = ["title", "rank", "description", "year"]
        widgets = {
            "title": TextInput(attrs={"placeholder": "Contoh: OSN-K Informatika", "maxlength": 255}),
            "rank": TextInput(attrs={"placeholder": "Contoh: Juara 1", "maxlength": 100}),
            "description": Textarea(attrs={"placeholder": "Ceritakan pencapaianmu di sini...", "rows": 3}),
            "year": NumberInput(attrs={"placeholder": "Contoh: 2024"}),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "category", "description", "ended_at"]
        widgets = {
            "title": TextInput(attrs={"placeholder": "Contoh: Project Officer SSG", "maxlength": 255}),
            "category": Select(),
            "description": Textarea(attrs={"placeholder": "Jelaskan peranmu...", "rows": 3}),
            "ended_at": DateInput(attrs={"type": "date"}),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "period"]
        widgets = {
            "institution": TextInput(attrs={"placeholder": "Contoh: Universitas Indonesia", "maxlength": 255}),
            "degree": TextInput(attrs={"placeholder": "Contoh: S1 Ilmu Komputer", "maxlength": 255}),
            "period": TextInput(attrs={"placeholder": "Contoh: 2025 - Sekarang", "maxlength": 100}),
        }

class CertificationForm(ModelForm):
    class Meta:
        model = Certification
        fields = ["title", "issuer", "issue_date"]
        widgets = {
            "title": TextInput(attrs={"placeholder": "Contoh: Art & Design Fundamentals", "maxlength": 255}),
            "issuer": TextInput(attrs={"placeholder": "Contoh: Coursera", "maxlength": 255}),
            "issue_date": DateInput(attrs={"type": "date"}),
        }