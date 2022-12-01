# Generated by Django 4.1.3 on 2022-12-01 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parser_hh', '0005_rename_user_vacancy_vacancy_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='param',
            name='author',
        ),
        migrations.AddField(
            model_name='param',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]