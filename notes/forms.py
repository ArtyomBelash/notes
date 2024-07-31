from django import forms
from .models import Note


class NoteCreateAndUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'description')
