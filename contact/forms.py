from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    # first_name = forms.CharField(label = 'Primeiro nome')
    # last_name = forms.CharField(label = 'Sobrenome')
    # phone = forms.CharField(label = 'Telefone')

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'description', 'category']
    
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     self.add_error(
    #         'first_name',
    #         ValidationError('Error', code='invalid')
    #         )
    #     return super().clean()
