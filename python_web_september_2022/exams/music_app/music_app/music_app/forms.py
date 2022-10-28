from django import forms

from MusicApp.music_app.models import ProfileModel, AlbumModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['username', 'email', 'age']

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email'}
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': 'Age'}
            ),
        }

    def clean(self):
        return super().clean()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'

    widgets = {
        'album_name': forms.TextInput(
            attrs={'placeholder': 'Album Name'}
        ),
        'artist': forms.TextInput(
            attrs={'placeholder': 'Artist'}
        ),
        'genre': forms.ChoiceField(),
        'description': forms.TextInput(
            attrs={'placeholder': 'Description'}
        ),
        'image_url': forms.URLInput(
            attrs={'placeholder': 'Image URL'}
        ),
        'price': forms.NumberInput(
            attrs={'placeholder': 'Price'}
        ),

    }

    def clean(self):
        return super().clean()


class DeleteAlbumForm(CreateAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
