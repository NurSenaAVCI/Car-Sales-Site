from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
from django.utils.text import slugify

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':"E-mail Please"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password Please'}))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username','email','password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username Please'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail Please'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Please'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again Please'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','city','phone']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        widgets = {
            'name':forms.TextInput(attrs={'class' : 'form-control'}),
            'city':forms.TextInput(attrs={'class' : 'form-control'}),
            'phone':forms.TextInput(attrs={'class' : 'form-control'}),
        }

class PasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'})

        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'})

        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password Again'})

class UserInformationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

