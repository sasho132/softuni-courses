from django.urls import path

from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='add-pet'),
    path('details/', views.delete_pet, name='delete-pet'),

]
