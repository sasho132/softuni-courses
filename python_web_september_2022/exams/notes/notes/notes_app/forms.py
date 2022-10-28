from django import forms

from notes.notes_app.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'age': forms.NumberInput(),
        }


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(),
            'content': forms.Textarea(),
            'image_url': forms.URLInput(),
        }


class DeleteNoteForm(CreateNoteForm):
    def __init__(self, *args, **kwargs):
        super(DeleteNoteForm, self).__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for (_, field) in self.fields.items():
            field.required = False
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
