
import datetime
from core.models import Server
from postgres.models import DataBase
from django import forms
# from django.contrib.auth.models import User

class BackupForm(forms.Form):
    # date = forms.DateField(initial=datetime.datetime.today,required=True)
    description = forms.CharField(max_length=30,required=True)
    database = forms.ModelChoiceField(queryset=DataBase.objects.all(),required=True)


