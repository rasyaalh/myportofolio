from django.utils.html import strip_tags
from rest_framework import serializers
from main.models import Experience, Achievement, Education, Certification

class BaseStarSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())

    def clean_text(self, value):
        val = strip_tags(str(value)).strip()
        if not val:
            raise serializers.ValidationError("Field ini tidak boleh kosong.")
        return val

class ExperienceSerializer(BaseStarSerializer):
    class Meta:
        model = Experience
        fields = ["id", "title", "category", "description", "ended_at", "star_count", "is_starred", "starred_by_names"]
        read_only_fields = ["id"]
    def validate_title(self, value): return self.clean_text(value)
    def validate_description(self, value): return strip_tags(value)

class AchievementSerializer(BaseStarSerializer):
    class Meta:
        model = Achievement
        fields = ["id", "title", "rank", "description", "year", "star_count", "is_starred", "starred_by_names"]
        read_only_fields = ["id"]
    def validate_title(self, value): return self.clean_text(value)
    def validate_rank(self, value): return self.clean_text(value)
    def validate_description(self, value): return strip_tags(value)

class EducationSerializer(BaseStarSerializer):
    class Meta:
        model = Education
        fields = ["id", "institution", "degree", "period", "star_count", "is_starred", "starred_by_names"]
        read_only_fields = ["id"]
    def validate_institution(self, value): return self.clean_text(value)
    def validate_degree(self, value): return self.clean_text(value)
    def validate_period(self, value): return self.clean_text(value)

class CertificationSerializer(BaseStarSerializer):
    class Meta:
        model = Certification
        fields = ["id", "title", "issuer", "issue_date", "star_count", "is_starred", "starred_by_names"]
        read_only_fields = ["id"]
    def validate_title(self, value): return self.clean_text(value)
    def validate_issuer(self, value): return self.clean_text(value)