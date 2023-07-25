from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from auth.models import User

# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, label='email')
#     username = forms.CharField(label='username', min_length=5, max_length=150)
#     name = forms.CharField(label='name')
#     password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ("username", "name", "email", "password1", "password2", "status")

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.username = self.cleaned_data['username']
#         user.status = "user"
#         if commit:
#             user.save()
#         return user