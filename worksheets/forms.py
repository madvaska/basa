from django import forms
from .models import WorksheetFile

class WFForm(forms.ModelForm):
    class Meta:
        model = WorksheetFile
        fields = ('original','fileName',)
