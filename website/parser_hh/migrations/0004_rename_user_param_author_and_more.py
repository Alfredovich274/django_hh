# Generated by Django 4.1.3 on 2022-11-30 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_hh', '0003_vacancy_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='param',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='user',
            new_name='user_vacancy',
        ),
    ]