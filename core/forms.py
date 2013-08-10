
from core.models import *
from django import forms
from django.utils.translation import ugettext as _
# from django.contrib.auth.models import User

class ServerForm(forms.Form):
    # date = forms.DateField(initial=datetime.datetime.today,required=True)
    name = forms.CharField("name", required=True)
    host = forms.CharField("host", required=True)
    description = forms.CharField(widget=forms.Textarea, max_length=300,required=True)
    #database = forms.ModelChoiceField(queryset=DataBase.objects.all(),required=True)



