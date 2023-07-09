from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # IMPORTANT AF
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Display Name', 'maxlength': '30'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'password1': forms.PasswordInput(
                attrs={'class': 'form-control password-input', 'placeholder': 'Email Address'}),
            'password2': forms.PasswordInput(
                attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password1'].error_message = 'AAAA'
        self.fields['password2'].help_text = ''
