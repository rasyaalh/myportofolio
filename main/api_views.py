from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Experience, Achievement, Education, Certification
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import ExperienceSerializer, AchievementSerializer, EducationSerializer, CertificationSerializer

def generic_list_create(request, model_class, serializer_class, search_field=None):
    if request.method in ("GET", "HEAD"):
        qs = model_class.objects.prefetch_related("starred_by").all()
        if search_field:
            query = request.query_params.get(search_field, "").strip()
            if query:
                qs = qs.filter(**{f"{search_field}__icontains": query})
        serializer = serializer_class(qs, many=True, context={"request": request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

def generic_detail(request, obj, serializer_class):
    if request.method in ("GET", "HEAD"):
        return Response(serializer_class(obj, context={"request": request}).data)
    elif request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = serializer_class(obj, data=request.data, partial=(request.method == "PATCH"), context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

def generic_star(request, obj, serializer_class):
    if obj.starred_by.filter(pk=request.user.pk).exists():
        obj.starred_by.remove(request.user)
    else:
        obj.starred_by.add(request.user)
    return Response(serializer_class(obj, context={"request": request}).data)

# --- VIEWS ROUTING ---
@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_list(request): return generic_list_create(request, Experience, ExperienceSerializer, "title")

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_detail(request, experience_id): return generic_detail(request, get_object_or_404(Experience, pk=experience_id), ExperienceSerializer)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def experience_star(request, experience_id): return generic_star(request, get_object_or_404(Experience, pk=experience_id), ExperienceSerializer)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def achievement_list(request): return generic_list_create(request, Achievement, AchievementSerializer, "title")

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def achievement_detail(request, achievement_id): return generic_detail(request, get_object_or_404(Achievement, pk=achievement_id), AchievementSerializer)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def achievement_star(request, achievement_id): return generic_star(request, get_object_or_404(Achievement, pk=achievement_id), AchievementSerializer)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_list(request): return generic_list_create(request, Education, EducationSerializer, "institution")

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_detail(request, education_id): return generic_detail(request, get_object_or_404(Education, pk=education_id), EducationSerializer)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def education_star(request, education_id): return generic_star(request, get_object_or_404(Education, pk=education_id), EducationSerializer)


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def certification_list(request): return generic_list_create(request, Certification, CertificationSerializer, "title")

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def certification_detail(request, certification_id): return generic_detail(request, get_object_or_404(Certification, pk=certification_id), CertificationSerializer)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def certification_star(request, certification_id): return generic_star(request, get_object_or_404(Certification, pk=certification_id), CertificationSerializer)