from django import forms
from django.forms import ModelForm
from .models import User, Numbers


# class UserForm(forms.Form):
#     name = forms.CharField(max_length=100,
#                                  widget = forms.TextInput(attrs = {'placeholder': ('Name')}))
#     email = forms.EmailField(max_length=100,
#                              widget = forms.TextInput(attrs = {'placeholder': ('E-mail')}))
#     password = forms.CharField(max_length=32,
#                                widget = forms.PasswordInput(attrs = {'placeholder': ('Password')}))
#     mobile = forms.CharField(max_length=100,
#                              widget = forms.TextInput(attrs = {'placeholder': ('Mobile No.')}))


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class NumberModelForm(ModelForm):
    class Meta:
        model = Numbers
        fields = ['mobile']