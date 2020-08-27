from django import forms

class UserRegister(forms.Form):
	username = forms.CharField(max_length = 20)
	email = forms.EmailField()
	password = forms.CharField(max_length = 20, widget = forms.PasswordInput())



class UserLogin(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20, widget = forms.PasswordInput())