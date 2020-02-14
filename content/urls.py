from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<slug>/', views.post_detail, name='post_detail'),
]
