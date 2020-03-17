from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'display_name', 'first_name', 'last_name', 'phone_number',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'email', 'display_name', 'password', 'first_name', 'last_name', 'phone_number', 'is_active',
            'is_staff'
        )

    def clean_password(self):
        # Password can't be changed in the admin
        return self.initial["password"]
