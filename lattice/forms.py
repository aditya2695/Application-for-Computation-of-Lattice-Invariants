from django import forms
from .models import latticeEntries

class LatticeForm(forms.ModelForm):

    model = latticeEntries
    fields =  ('a','b','c','alpha','beta','gamma')   


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()