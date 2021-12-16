from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm


class RegistrationForm(UserCreationForm):
   email = forms.EmailField(
      max_length=100,
      required=True,
      widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

   password1 = forms.CharField(
      label='password',
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

   password2 = forms.CharField(
      label='confirm Password (Again)',
      widget=forms.PasswordInput(
         attrs={'class': 'form-control', 'placeholder': 'Password Again'})
   )

   class Meta:
      model = User
      fields = [
         'username', 'email', 'password1', 'password2']
      labels = {'email': 'Email'}
      widgets = {'username':
                  forms.TextInput(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
   username = UsernameField(widget=forms.TextInput(
      attrs={'autofocus': True, 'class': 'form-control'}))

   password = forms.CharField(label=("password"), strip=False,
                              widget=forms.PasswordInput(attrs={'autocomplete': 'curent-password', 'class': 'form-control'}))



