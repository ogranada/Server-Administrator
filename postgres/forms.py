
import datetime
from django import forms
from django.contrib.auth.models import User

class BackupForm(forms.Form):
    # date = forms.DateField(initial=datetime.datetime.today,required=True)
    description = forms.CharField(max_length=30,required=True)
    # user = forms.ModelChoiceField(queryset=User.objects.all(),required=True)


