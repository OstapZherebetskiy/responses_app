from django import forms

from .models import Areas, Places, Comments

class PlacesForm(forms.ModelForm):
    class Meta:
        
        model = Places
        fields = ['text']
        labels = {'text': 'Place:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class CommentsForm(forms.ModelForm):
    class Meta:
        
        model = Comments
        fields = ['text', 'file']
        labels = {'text': 'Comment:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
