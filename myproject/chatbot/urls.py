from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_page_view, name='chatbot_page'),
    path('chatbot/', views.chatbot_view, name='chatbot' )
]
