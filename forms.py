from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *


class ReviewForms(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Ваш отзыв...'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвеодите пароль'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша фамилия'
            })
        }


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'region', 'phone']
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш адрес'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            'region': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Регион'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            })
        }
