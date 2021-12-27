from django import forms
from django.core.exceptions import ValidationError
from .models import Word

class NewWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = [
            'first_language',
            'second_language'
        ]
        widgets = {
            'first_language' : forms.TextInput({'class' : 'word_form'}),
            'second_language' : forms.TextInput({'class' : 'word_form'})
        }

    def clean_first_language(self):
        first_language = self.cleaned_data['first_language']
        if len(first_language) > 20:
            raise ValidationError('Длина слова превышает 20 символов')
        return first_language

    def clean_second_language(self):
        second_language = self.cleaned_data['second_language']
        if len(second_language) > 30:
            raise ValidationError('Длина слова превышает 30 символов')
        return second_language