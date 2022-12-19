from django.urls import path, include
from .models import City, Skill, Param, Experience
from .serializers import CitySerializer, SkillSerializer, ParamSerializer
from .serializers import ExperienceSerializer
from rest_framework import viewsets
from .permissions import IsAuthor, ReadOnly
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication


# ViewSets define the view behavior.
class CityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]  # классы прав доступа к api
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ParamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsAuthor | ReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Param.objects.all()
    serializer_class = ParamSerializer
