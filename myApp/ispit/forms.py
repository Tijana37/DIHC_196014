from django import forms
from .models import *


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        exclude = ('id', 'user_created',)