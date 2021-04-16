from django import forms
from apps.orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name',  'number', 'email', 'district', 'city', 'address', 'post_code', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                   'id': 'first',
                                                   'name': 'name',
                                                   'placeholder': 'Имя',
                                                   'required': 'true'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                  'id': 'last',
                                                  'name': 'name',
                                                  'placeholder': 'Фамилия',
                                                  'required': 'true'}),
            'number': forms.TextInput(attrs={'class': 'form-control',
                                               'id': 'number',
                                               'name': 'number',
                                               'placeholder': 'Телефон',
                                               'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                              'id': 'email',
                                              'name': 'compemailany',
                                              'placeholder': 'Email',
                                              'required': 'true'}),
            'district': forms.TextInput(attrs={'class': 'form-control',
                                                 'id': 'add1',
                                                 'name': 'add1',
                                                 'placeholder': 'Область',
                                                 'required': 'true'}),
            'city': forms.TextInput(attrs={'class': 'form-control',
                                             'id': 'city',
                                             'name': 'city',
                                             'placeholder': 'Город',
                                             'required': 'true'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                                'id': 'add2',
                                                'name': 'add2',
                                                'placeholder': 'Адрес',
                                                'required': 'true'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control',
                                                  'id': 'zip',
                                                  'name': 'zip',
                                                  'placeholder': 'Почтовый индекс',
                                                  'required': 'true'}),
            'comment': forms.Textarea(attrs={'class': 'form-control',
                                                'id': 'message',
                                                'name': 'message',
                                                'placeholder': 'Комментарии к заказу',
                                                'rows': '1'})
        }
