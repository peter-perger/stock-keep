from django import forms
from django.contrib.auth.models import User
from .models import Product

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150, help_text="")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        
        return cleaned_data


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", 'quantity', 'supplier']

    def clean(self):
        cleaned_data =  super().clean()
        return cleaned_data
    