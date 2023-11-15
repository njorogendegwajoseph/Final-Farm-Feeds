from django import forms
from .models import Subscription
from .models import Order


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'quantity', 'customer_name',
                  'contact_number', 'email', 'additional_notes']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['customer_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['contact_number'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['additional_notes'].widget.attrs.update(
            {'class': 'form-control', 'rows': '4'})
