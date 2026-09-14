from django.urls import path
from main.views import (
    show_main, 
    show_experience, 
    show_achievements, 
    show_education, 
    show_certifications
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    
    #TUGAS 2
    path("achievements/", show_achievements, name="show_achievements"),
    path("education/", show_education, name="show_education"),
    path("certifications/", show_certifications, name="show_certifications"),
]