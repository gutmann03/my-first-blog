from django.urls import path
from . import views
from .models import Post

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('menu/', views.get_menu, name='menu'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]