from django import forms

from games_play.games_app.models import Profile, Game


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class DeleteProfile(EditProfile):
    def __init__(self, *args, **kwargs):
        super(DeleteProfile, self).__init__(*args, **kwargs)
        self.__hidden_fields()

    def __hidden_fields(self):
        for (_, field) in self.fields.items():
            field.required = False
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class DeleteGame(CreateGame):
    def __init__(self, *args, **kwargs):
        super(DeleteGame, self).__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for (_, field) in self.fields.items():
            field.required = False
            field.widget.attrs['disable'] = 'disable'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
