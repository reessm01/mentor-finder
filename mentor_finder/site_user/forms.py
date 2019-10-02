from django.contrib.auth.models import User
from django import forms

from mentor_finder.personality.models import Personality
from mentor_finder.industry.models import Industry

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    personality = forms.ModelChoiceField(queryset=Personality.objects.all())
    industry = forms.ModelChoiceField(queryset=Industry.objects.all())
    is_mentor = forms.BooleanField(initial=False, required=False, label='Sign up as a mentor.')