from django import forms
from apps.orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    number = forms.CharField(required=True)
    email = forms.CharField(required=True)
    district = forms.CharField(required=True)
    city = forms.CharField(required=True)
    address = forms.CharField(required=True)
    post_code = forms.CharField(required=True)
    comment = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name',  'number', 'email', 'district', 'city', 'address', 'post_code', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарии к заказу'})
        }
