from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloglist_view, name = "blogs"),
    path('blogform', views.blogform_view, name = "blogform"),
    path('editblog/<slug:slug>/', views.editblog_view, name = "editblog"),
    path('deleteblog/<slug:slug>/', views.deleteblog_view, name = "deleteblog"),
    path('blog/<slug:slug>/', views.blog_view, name = "blogview"),
]
