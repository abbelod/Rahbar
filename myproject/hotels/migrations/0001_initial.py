# Generated by Django 5.1.3 on 2024-11-20 17:30

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
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, default='default_hotel.png', upload_to='images/hotel_images/')),
                ('amenities', models.TextField(blank=True, help_text='Comma-separated list of amenities')),
                ('available_rooms', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_listings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
