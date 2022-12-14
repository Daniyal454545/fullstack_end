# Generated by Django 4.1.2 on 2022-11-04 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('photo', models.ImageField(upload_to='shop_photo')),
                ('description', models.CharField(blank=True, max_length=500)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
# 