from django import forms
from .models import Cliente
from django.views.generic import ListView

class test(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','telefone','cpf','endereco']

