from django import forms

from GamesPlayApp.games_play_app.models import ProfileModel, GameModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']

        widgets = {
            'email': forms.TextInput(
                attrs={'placeholder': 'Email'}
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': 'Age'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Password'}
            ),
        }

    def clean(self):
        return super().clean()

        # def clean_data(self):
        #     return self.cleaned_data['email', 'age', 'password']


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'

    def clean(self):
        return super().clean()


class DeleteGameForm(GameCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

        widgets = {
            'email': forms.TextInput(
                attrs={'placeholder': 'Email'}
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': 'Age'}
            ),
            # 'password': forms.PasswordInput(
            #     attrs={'placeholder': 'Password'}
            # ),
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name'}
            ),
            'profile_picture': forms.URLInput(
                attrs={'placeholder': 'URL'}
            ),
        }

    def clean(self):
        return super().clean()
