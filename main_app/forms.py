from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','userType']
    
class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length = 64)
    password = forms.CharField(widget = forms.PasswordInput())
