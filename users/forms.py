from django import forms
from django.core import exceptions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.forms import widgets
from .models import User

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("name","email")
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }

    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}), validators=[validate_password])
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}), label="Comfirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("User already exist with this email")
        except User.DoesNotExist:
            return email
            
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)  # create object, but object hasn't yet been saved to the database 
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()
