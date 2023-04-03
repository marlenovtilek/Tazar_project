from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm

from main.models import User, CollectionPlaces, MaterialType


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget= forms.TextInput(
            attrs = {"class":"form-control"}
        )
    )
    password = forms.CharField(
        label = "Пароль",
        widget = forms.PasswordInput(
            attrs = {"class":"form-control"}
        )
    )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label = "Пароль",
        widget = forms.PasswordInput(
            attrs = {"class":"form-control"}
        )
    )
    password2 = forms.CharField(
        label = "Повторите пароль:",
        widget = forms.PasswordInput(
            attrs = {"class":"form-control"}
        )   
    )


    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone"
        ]
        form_control = {"class":"form-control"}
        widgets = {
            "username":forms.TextInput(attrs=form_control),
            "first_name":forms.TextInput(attrs=form_control),
            "last_name":forms.TextInput(attrs=form_control),
            "email": forms.EmailInput(attrs=form_control),
            "phone": forms.TextInput(attrs=form_control),
        }

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            "avatar",
            "email",
            "first_name",
            "last_name",
            "phone"
        )
        widgets = {
            "avatar": forms.FileInput(
                attrs={"class":"form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"class":"form-control"}
            ),
            "first_name": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "phone": forms.TextInput(
                attrs={"class":"form-control"}
            )  
        }


class UserPasswordChangeForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = CollectionPlaces
        fields = (
            "name", 
            "address", 
            "phone", 
            "working_hours", 
            "photo", 
            "email", 
            "material_type"
            )

        widgets = {
            "name": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "addres": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "phone": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "working_hours": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "photo": forms.FileInput(
                attrs={"class":"form-control"}
            ),
            "email": forms.TextInput(
                attrs={"class":"form-control"}
            ),
            "material_type": forms.CheckboxSelectMultiple(
                attrs={"class":"form-control"}
            )
        }

    material_types = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        queryset = MaterialType.objects.all(),
        required = False
    )   