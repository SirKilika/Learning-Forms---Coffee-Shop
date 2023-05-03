from django import forms
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from .models import UserDetails

from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


class NameForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)

    def save(self):
        pass


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        error_messages = {
            "username": {
                "unique": ("Please enter another username. This one is taken."),
            },
        }

    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get("password"))
        m.username = self.cleaned_data.get("username").lower()

        if commit:
            m.save()
        return m


class UserDetailsForm(ModelForm):
    lastName = forms.CharField(required=False)

    class Meta:
        model = UserDetails
        fields = "__all__"
        error_messages = {
            "zipcode": {
                "invalid_length": _("Wrong zipcode. It needs to be 4 characters long"),
            },
        }

    def clean(self):
        address = self.cleaned_data.get("address")
        zipcode = self.cleaned_data.get("zipcode")

        if address and zipcode:
            if zipcode > "1234":
                msg = "We do not deliver in the area"
                self.add_error("address", msg)
                self.add_error("zipcode", msg)
                raise ValidationError(("There's a problem with the address entered"),
                                      code="wrong_address")

