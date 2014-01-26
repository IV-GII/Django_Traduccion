# /uploadering/filebaby/forms.py

from django import forms

from filebaby.models import FilebabyFile


class FilebabyForm(forms.ModelForm):
    """Upload files with this form"""
    class Meta:
        model = FilebabyFile
        exclude = ('md5',)
