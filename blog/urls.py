from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('<str:title>/', views.post_detail_by_title, name="post_detail_by_title")
]