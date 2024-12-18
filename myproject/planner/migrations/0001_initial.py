# Generated by Django 5.1.3 on 2024-12-03 18:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attractions', to='planner.itinerary')),
            ],
        ),
        migrations.CreateModel(
            name='TravelRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location', models.CharField(max_length=255)),
                ('end_location', models.CharField(max_length=255)),
                ('travel_mode', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='planner.itinerary')),
            ],
        ),
    ]
