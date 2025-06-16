from django import forms
from .models import Review
from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'content'] 


class SignUpForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Иван Иванов',
        'required': 'required'
    }))
    phone = forms.CharField(label='Телефон', max_length=20, widget=forms.TextInput(attrs={
        'placeholder': '+7 (999) 123-45-67',
        'required': 'required'
    }))
    email = forms.EmailField(label='Email (необязательно)', required=False, widget=forms.EmailInput(attrs={
        'placeholder': 'email@example.com'
    }))
    training_id = forms.IntegerField(widget=forms.HiddenInput())
    training_type = forms.CharField(widget=forms.HiddenInput())


class CallbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    phone = forms.CharField(max_length=20, label='Телефон')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))