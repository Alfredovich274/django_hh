from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import UserHh
from django.urls import reverse_lazy


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):
    model = UserHh
    template_name = 'userapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login')
