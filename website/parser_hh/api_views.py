from django.urls import path, include
from .models import City, Skill, Param, Experience
from .serializers import CitySerializer, SkillSerializer, ParamSerializer
from .serializers import ExperienceSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ParamViewSet(viewsets.ModelViewSet):
    queryset = Param.objects.all()
    serializer_class = ParamSerializer
