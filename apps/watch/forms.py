from django import forms
from apps.orders.models import OrderDetail


class ProductForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['count', ]
        widgets = {
            'count': forms.NumberInput(attrs={'class': 'product_count_item input-number'}),
        }
