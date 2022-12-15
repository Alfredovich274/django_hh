from django.urls import path, include
from .models import City, Skill, Param, Experience, Schedule
from userapp.models import UserHh
from rest_framework import serializers


# Serializers define the API representation.
class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        # fields = ['url', 'username', 'email', 'is_staff']


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'name']


class ParamSerializer(serializers.HyperlinkedModelSerializer):
    experience = serializers.PrimaryKeyRelatedField(queryset=Experience.objects.all(), required=False)
    schedule = serializers.PrimaryKeyRelatedField(queryset=Schedule.objects.all(), required=False)
    author = serializers.PrimaryKeyRelatedField(queryset=UserHh.objects.all(), required=False)

    class Meta:
        model = Param
        fields = '__all__'
