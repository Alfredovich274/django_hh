from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserHh(AbstractUser):
    #  email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # ни чего не возвращает
        if not Profile.objects.filter(user=self).exists():  # Если профиль не создан
            Profile.objects.create(user=self)  # Создаем профиль


class Profile(models.Model):
    user = models.OneToOneField(UserHh, on_delete=models.CASCADE)
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    nickname = models.TextField(blank=True)
    info = models.TextField(blank=True)


@receiver(post_save, sender=UserHh)
def create_profile(sender, instance, **kwargs):
    print('Сработал обработчик сигнала')
#     if not Profile.objects.filter(user=instance).exists():
#         Profile.objects.create(user=instance)
