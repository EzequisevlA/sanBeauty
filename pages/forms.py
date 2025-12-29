from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'second_name', 'professional', 'services', 'date', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'second_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'professional': forms.Select(),
            'services': forms.SelectMultiple(),
        }
