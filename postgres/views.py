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

from hashlib import md5

@login_required
def index(request):
    return render_to_response('postgres/index.html', context_instance=RequestContext(request))

@login_required
def backup(request):
    c = {}
    c.update(csrf(request))
    c["backupForm"] = BackupForm()
    return render_to_response('postgres/backup.html', c, context_instance=RequestContext(request))

@login_required
@ajax_view
def savebackup(request):
    c = {}
    if request.is_ajax():
        form = BackupForm(request.GET)
        if form.is_valid():
            bkp = Backup()
            bkp.description = form.cleaned_data['description']
            bkp.database = form.cleaned_data['database']
            bkp.user_id = request.user.id
            bkp.save()
            try:
                basename = md5(str(bkp.date)).hexdigest()
                filename = basename + '.dump'
                success, msj = run_pgDump(filename, bkp.database.server.host, bkp.database.name, bkp.database.username, bkp.database.password)
                if success:
                    c['status'] = 'Ok'
                    c['message'] = filename + " Saved"
                    objs = ''.join(['<option value="%i">%s</option>'%(x.id,x.description) for x in Backup.objects.all()])
                    c['objects'] = objs
                else:
                    c['status'] = 'Fail'
                    c['message'] = "Error: " + msj
            except Exception as w:
                c['status'] = 'Fail'
                c['message'] = "Error(" + str(type(w)) + "): " + str(w)
        else:
            c['status'] = 'Fail'
            c['message'] = str(form.errors)
    return c


@login_required
def databases(request):
    c = {}
    c['dbFrm'] = DatabaseForm()
    return render_to_response('postgres/databases.html', c, context_instance=RequestContext(request))

@login_required
@ajax_view
def restore_backup(request, num=-1):
    if num != -1:
        try:
            return {"response": "Done"}
        except Exception as w:
            return {"response": 'Error (' + type(w) + '):'+str(w)}
    else:
        return {"response": 'incorrect value'}

@login_required
@ajax_view
def savedatabase(request):
    if request.is_ajax():
        try:
            db = DataBase()
            db.server_id = request.GET['server']
            db.name = request.GET['name']
            db.schema = request.GET['schema']
            db.username = request.GET['username']
            db.password = request.GET['password']
            db.user = request.user
            db.save()
            return {'status':'Ok','message':'Server Saved'}
        except Exception as e:
            return {'status':'Fail','message':'Error Saving: ' + str(e)}