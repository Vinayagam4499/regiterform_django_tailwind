from django import forms
from .models import Person  # Import the Person model

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'phone_number', 'address']
