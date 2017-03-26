from django import forms

class RegisterForm(forms.Form):
    user_id = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)

class NewListingForm(forms.Form):
    make = forms.CharField(label='make', max_length=100)
    model = forms.CharField(label='model', max_length=100)
    year = forms.IntegerField(label='year')
    color = forms.CharField(label='color', max_length=100)
    body_type = forms.CharField(label='body_type', max_length=100)
    num_seats = forms.IntegerField(label='num_seats')