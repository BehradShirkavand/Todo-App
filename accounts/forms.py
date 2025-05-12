from django import forms


class UserRegisterationForm(forms.Form):
    first_name = forms.CharField()
    last_name= forms.CharField()
    username= forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()

class UserLoginForm(forms.Form):
    username= forms.CharField()
    password = forms.CharField()