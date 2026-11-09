from django.urls import path
from main import api_views

app_name = "api"

urlpatterns = [
    path("experience/", api_views.experience_list, name="experience-list"),
    path("experience/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experience/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),

    path("achievement/", api_views.achievement_list, name="achievement-list"),
    path("achievement/<uuid:achievement_id>/", api_views.achievement_detail, name="achievement-detail"),
    path("achievement/<uuid:achievement_id>/star/", api_views.achievement_star, name="achievement-star"),

    path("education/", api_views.education_list, name="education-list"),
    path("education/<uuid:education_id>/", api_views.education_detail, name="education-detail"),
    path("education/<uuid:education_id>/star/", api_views.education_star, name="education-star"),

    path("certification/", api_views.certification_list, name="certification-list"),
    path("certification/<uuid:certification_id>/", api_views.certification_detail, name="certification-detail"),
    path("certification/<uuid:certification_id>/star/", api_views.certification_star, name="certification-star"),
]