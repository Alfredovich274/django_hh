from django.contrib.auth.forms import UserCreationForm
from .models import UserHh


class RegistrationForm(UserCreationForm):

    class Meta:
        model = UserHh
        fields = ('username', 'password1', 'password2', 'email')
