from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.timezone import now
from ckeditor.fields import RichTextField

class Blog(models.Model):
    # Basic fields for a blog
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to='images/blog_images', blank=True, null=True, default='images/blog_images//default_blog.png')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # Additional fields
    is_published = models.BooleanField(default=False)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")

    def save(self, *args, **kwargs):
        # Automatically generate a slug based on the title
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
