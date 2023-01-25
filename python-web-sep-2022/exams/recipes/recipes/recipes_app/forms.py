from django import forms

from recipes.recipes_app.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(),
            'image_url': forms.URLInput(),
            'description': forms.Textarea(),
            'ingredients': forms.TextInput(),
            'time': forms.TimeInput(),
        }


class DeleteRecipeForm(CreateRecipeForm):
    def __init__(self, *args, **kwargs):
        super(DeleteRecipeForm, self).__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for (_, field) in self.fields.items():
            field.required = False
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
