from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['foto', 'nome', 'quantidade', 'preco']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['foto'].widget.attrs.update({'class': 'form-control', 'accept': 'image/*'})
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['preco'].widget.attrs.update({'class': 'form-control'})
