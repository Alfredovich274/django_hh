# Generated by Django 4.1.3 on 2022-11-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_userhh_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhh',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
