
import datetime
from core.models import Server
from postgres.models import DataBase
from django import forms
# from django.contrib.auth.models import User

class BackupForm(forms.Form):
    description = forms.CharField(max_length=30,required=True)
    database = forms.ModelChoiceField(queryset=DataBase.objects.all(),required=True)

class DatabaseForm(forms.Form):
    server = forms.ModelChoiceField(queryset=Server.objects.all(),required=True)
    name = forms.CharField(max_length=30,required=True)
    schema = forms.CharField(max_length=30,required=True)
    username = forms.CharField(max_length=30,required=True)
    password = forms.CharField(widget=forms.PasswordInput, max_length=30, required=True)


