from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'tipo_documento', 'documento', 'email', 'endereco']
        labels = {
            'nome': 'Nome completo',
            'tipo_documento': 'Tipo de documento',
            'documento': 'CPF/CNPJ',
            'email': 'Endereço de email',
            'endereco': 'Endereço completo',
        }
        widgets = {
            'tipo_documento': forms.RadioSelect(choices=[('CPF', 'CPF'), ('CNPJ', 'CNPJ')])
        }