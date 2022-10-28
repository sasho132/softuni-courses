from django.urls import path

from notes.notes_app.views import index, add_note, edit_note, delete_note, details_note, profile_details, delete_profile

urlpatterns = [
    path('', index, name='home-page'),
    path('add/', add_note, name='add-note'),
    path('edit/<int:pk>', edit_note, name='edit-note'),
    path('delete/<int:pk>', delete_note, name='delete-note'),
    path('details/<int:pk>', details_note, name='details-note'),
    path('profile/', profile_details, name='profile-details'),
]
