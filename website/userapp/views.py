from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView
from .models import UserHh
from django.urls import reverse_lazy, reverse
from rest_framework.authtoken.models import Token
from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):
    model = UserHh
    template_name = 'userapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login')


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'userapp/profile.html'
    model = UserHh


def update_token(request):
    user = request.user
    try:
        if user.auth_token:
            user.auth_token.delete()
    except:
        pass
    Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('user:profile', kwargs={'pk': user.pk}))


def update_token_ajax(request):
    user = request.user
    # если уже есть
    if user.auth_token:
        # обновить
        user.auth_token.delete()
        token = Token.objects.create(user=user)
    else:
        # создать
        token = Token.objects.create(user=user)
    return JsonResponse({'key': token.key})
