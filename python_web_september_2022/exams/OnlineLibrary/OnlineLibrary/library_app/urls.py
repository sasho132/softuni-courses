from django.urls import path, include

from OnlineLibrary.library_app.views import add_book, index, edit_book, details_book, profile_edit, \
    profile_delete, profile_details

urlpatterns = [
    path('', index, name='home-page'),
    path('add/', add_book, name='add-book'),
    path('edit/<int:pk>/', edit_book, name='edit-book'),
    path('details/<int:pk>/', details_book, name='details-book'),
    path('profile/', include([
       path('', profile_details, name='profile-details'),
       path('edit/', profile_edit, name='edit-profile'),
       path('delete/', profile_delete, name='delete-profile'),
    ])),
]
