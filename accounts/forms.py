from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from accounts.models import User

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('email', 'first_name',  'password1', 'password2')
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']

        if commit:
            user.save()
        return user

class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('first_name', 'avatar')

class PasswordChangeForm(PasswordChangeForm):
    def clean_new_password2(self):
        email = self.user.email
        new_password2 = self.cleaned_data.get('new_password2')

        validate_password(new_password2)

        return new_password2
