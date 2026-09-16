from django.urls import path
from main.views import * 

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    # Halaman Utama & Form
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("achievements/", show_achievements, name="show_achievements"),
    path("achievements/add/", create_achievement, name="create_achievement"),
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("certifications/", show_certifications, name="show_certifications"),
    path("certifications/add/", create_certification, name="create_certification"),

    # API JSON Endpoint
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("api/achievements/", get_achievements_json, name="get_achievements_json"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("api/certifications/", get_certifications_json, name="get_certifications_json"),

    # Fitur Hapus (Delete)
    path("experience/<str:id>/delete/", delete_experience, name="delete_experience"),
    path("achievements/<str:id>/delete/", delete_achievement, name="delete_achievement"),
    path("education/<str:id>/delete/", delete_education, name="delete_education"),
    path("certifications/<str:id>/delete/", delete_certification, name="delete_certification"),
]