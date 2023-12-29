from django import forms
from django.forms import ClearableFileInput

class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True 

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result 

class UploadAndCompressForm(forms.Form): 
    files = MultipleFileField(label="Select files to compress") 
    text = forms.CharField(max_length=100, label="Enter text for aaa.txt")
