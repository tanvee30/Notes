from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=('note_title','note_content')
        widgets={
            'note_title':forms.TextInput(attrs={'class':'form-control my-3'}),
            'note_content':forms.Textarea(attrs={'class':'form-control my-3'}),
        }
        labels = {
            'note_content':'Write your notes here'
        }