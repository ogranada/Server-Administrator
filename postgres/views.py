# Create your views here.

from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from core.utils import ajax_view


from postgres.forms import *
from postgres.models import *

@login_required
def index(request):
    return render_to_response('postgres/index.html', context_instance=RequestContext(request))

@login_required
def backup(request):
    c = {}
    c.update(csrf(request))
    state = ""
    c["backupForm"] = BackupForm()
    if request.POST:
        if request.POST["button"].lower() == "save":
            form = BackupForm(request.POST)
            if form.is_valid():
                bkp = Backup()
                bkp.description = form.cleaned_data['description']
                bkp.user_id = request.user.id
                bkp.save()
                state = "Saved"
            else:
                state = str(form.errors) # "Invalid Data"
        elif request.POST["button"].lower() == "restore":
            print "restoring", Backup.objects.filter(id=request.POST["backups_id"])[0]
    c["state"] = state
    return render_to_response('postgres/backup.html', c, context_instance=RequestContext(request))

@login_required
@ajax_view
def restore_backup(request,num=-1):
    # from time import sleep
    # sleep(3)
    if num != -1:
        return {"user":request.user.username}
    else:
        return {"error":'incorrect value'}



