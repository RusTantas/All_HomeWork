from django import forms


class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Ваше логин')
    password = forms.CharField(max_length=8, label='Ваше пароль')
    password_2 = forms.CharField(max_length=8, label='Введите пароль повторно:')
    age = forms.IntegerField(label='Введите ваш возраст')
