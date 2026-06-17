from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control"}
        )
    )

    class Meta:

        model = User

        fields = [

            "username",

            "email",

            "password1",

            "password2",

        ]

        widgets = {

            "username": forms.TextInput(

                attrs={"class": "form-control"}

            ),

        }

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(

            attrs={"class": "form-control"}

        )

    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(

            attrs={"class": "form-control"}

        )

    )



class UpdateProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "first_name",
            "last_name"
        ]

        widgets = {

            "username": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),

            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "last_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

        }