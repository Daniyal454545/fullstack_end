# Generated by Django 4.1.2 on 2022-11-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_alter_person_age_alter_person_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(blank=True, max_length=10, verbose_name='Пол'),
        ),
    ]
# 