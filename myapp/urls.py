from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('text/<int:pk>/', views.text_content_detail, name='text_content_detail'),
    path('text/create/', views.text_content_create, name='text_content_create'),
    path('text/edit/<int:pk>/', views.text_content_edit, name='text_content_edit'),
]