from django import forms
from .models import userSignup,notes,contactus

class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'
    
class updateForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','city','state','mobile']

class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model=contactus
        fields='__all__'