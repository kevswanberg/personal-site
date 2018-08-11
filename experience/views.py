from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import WorkExperienceSerializer
from .models import WorkExperience


class ExperienceModelViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
