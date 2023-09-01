from django import forms


class Wanafunzi(forms.Form):
    firstname = forms.CharField(label="Enter your first name", max_length=30)
    lastname = forms.CharField(label="Enter your last name", max_length=30)
    email = forms.EmailField(label="Enter your email", max_length=30)
    upload_pic = forms.FileField()
