from django import forms

class RegisterForm(forms.Form):
    user_id = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)