from django import forms
from django.core.validators import MinValueValidator

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        validators=[MinValueValidator(1)],
        widget=forms.NumberInput(attrs={'min': '1'})
    )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)