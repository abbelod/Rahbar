# Generated by Django 5.1.3 on 2024-11-21 17:01

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
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the transport service.', max_length=100)),
                ('transport_type', models.CharField(choices=[('bus', 'Bus'), ('train', 'Train'), ('taxi', 'Taxi'), ('rental', 'Rental Vehicle'), ('other', 'Other')], help_text='Type of transport.', max_length=20)),
                ('capacity', models.PositiveIntegerField(help_text='Total passenger capacity.')),
                ('route', models.CharField(help_text='Route details (e.g., City A to City B).', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price per ticket or rental.', max_digits=10)),
                ('available_bookings', models.PositiveIntegerField(default=0, help_text='Number of seats currently available.')),
                ('image', models.ImageField(blank=True, help_text='Optional image of the transport service.', upload_to='transport/images')),
                ('description', models.TextField(blank=True, help_text='Additional information about the transport service.', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the listing was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the listing was last updated.')),
                ('created_by', models.ForeignKey(help_text='User who created this listing.', on_delete=django.db.models.deletion.CASCADE, related_name='transport_listings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transport Listing',
                'verbose_name_plural': 'Transport Listings',
            },
        ),
    ]
