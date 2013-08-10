# Create your views here.

from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from django.utils.translation import ugettext as _

from core.utils import ajax_view
from pg_utils import run_pgDump

from postgres.forms import *
from postgres.models import *

@login_required
def index(request):
    return render_to_response('postgres/index.html', context_instance=RequestContext(request))

@login_required
def backup(request):
    c = {}
    c.update(csrf(request))
    c['opresult'] = ''
    state = ""
    c["backupForm"] = BackupForm()
    if request.POST:
        if request.POST["button"].lower() == "save":
            form = BackupForm(request.POST)
            if form.is_valid():
                bkp = Backup()
                bkp.description = form.cleaned_data['description']
                bkp.database = form.cleaned_data['database']
                bkp.user_id = request.user.id
                bkp.save()
                try:
                    filename = str(bkp.date).replace(' ', '_').replace(":", '').split('.')[0] + '.dump'
                    # outfile, hostname, db, user, passwd
                    success, msj = run_pgDump(filename, bkp.database.server.host, bkp.database.name, bkp.database.username, bkp.database.password)
                    if success:
                        state = filename + " Saved"
                        c['opresult'] = 'ok'
                    else:
                        state = "Error: " + msj
                        c['opresult'] = 'err'
                except Exception as w:
                    state = "Error(" + str(type(w)) + "): " + str(w)
                    c['opresult'] = 'err'
            else:
                c['opresult'] = 'err'
                state = str(form.errors)  # "Invalid Data"
        elif request.POST["button"].lower() == "restore":
            print "restoring", Backup.objects.filter(id=request.POST["backups_id"])[0]
    c["state"] = state
    return render_to_response('postgres/backup.html', c, context_instance=RequestContext(request))

@login_required
@ajax_view
def restore_backup(request, num=-1):
    # from time import sleep
    # sleep(3)
    if num != -1:
        try:
            return {"response": "Done"}
        except Exception as w:
            return {"response": 'Error (' + type(w) + '):'+str(w)}
    else:
        return {"response": 'incorrect value'}



