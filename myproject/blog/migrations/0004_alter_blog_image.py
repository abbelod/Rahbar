# Generated by Django 5.1.3 on 2024-11-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='blog_images//default_blog.png', null=True, upload_to='images/blog_images'),
        ),
    ]
