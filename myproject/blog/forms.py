from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'tags', 'is_published']
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter the title of your blog'
        #     }),
        #     # 'content': forms.Textarea(attrs={
        #     #     'class': 'form-control',
        #     #     'placeholder': 'Write your blog content here...',
        #     #     'rows': 10
        #     # }),
        #     'image': forms.ClearableFileInput(attrs={
        #         'class': 'form-control'
        #     }),
        #     'tags': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter tags separated by commas (e.g., travel, adventure)'
        #     }),
        #     'is_published': forms.CheckboxInput(attrs={
        #         'class': 'form-check-input'
        #     }),
        # }
