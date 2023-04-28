from django import forms
from app.models import *

class Topic_Form(forms.ModelForm):

    class Meta:
        model=Topic
        fields='__all__'

class Webpage_Form(forms.ModelForm):

    class Meta:
        model=Webpage
        #fields='__all__'
        #fields=['Topic_Name', 'Name']
        exclude=['Email']
        help_texts={'Topic_Name':'Enter in a Capital case'}
        labels={'Topic_Name':'TN'}
        widgets={'url':forms.Textarea(attrs={'cols':20, 'rows':3})}

class AccessRecord_Form(forms.ModelForm):

    class Meta:
        model=AccessRecord
        fields='__all__'
