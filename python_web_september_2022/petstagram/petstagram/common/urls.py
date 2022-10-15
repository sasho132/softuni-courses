from django.urls import path

from petstagram.common import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('like/<int:photo_id>/', views.photo_like, name='photo-like'),
    path('share/<int:photo_id>/', views.photo_share, name='photo-share'),
]