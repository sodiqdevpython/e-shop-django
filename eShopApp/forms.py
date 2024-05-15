from django import forms
from .models import Order, Shipping

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['adress', 'contact_for', 'total_price', 'order']