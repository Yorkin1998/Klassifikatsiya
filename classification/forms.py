from django import forms
from .models import TextInput

class TextInputForm(forms.ModelForm):
    class Meta:
        model = TextInput
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Matn kiriting...'}),
        }
