from django import forms 

class NameForm(forms.Form):
	f_name = forms.CharField(label='first name', max_length=20)
	l_name = forms.CharField(label='last name', max_length=20)
	email = forms.CharField(label='email', max_length=20)
	phone = forms.CharField(label='phone number', max_length=20)
