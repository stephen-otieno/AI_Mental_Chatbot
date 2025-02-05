from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('user_name', 'user_email', 'user_password1', 'user_password2')

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        user_password1 = cleaned_data.get('user_password1')
        user_password2 = cleaned_data.get('user_password2')

        if user_password1 != user_password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
