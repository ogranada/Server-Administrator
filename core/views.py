# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout

from core.models import *

## TEMPLATE_CONTEXT_PROCESSORS

def menus(request):
    return {'menus': Applications.objects.all()}

def getuser(request):
    print "===>",request
    return {'user': request.user}

## END TEMPLATE_CONTEXT_PROCESSORS

def index(request):
    c = {}
    c["user"] = request.user
    return render_to_response("inicio.html", c)


def login(request):
    c = {}
    c.update(csrf(request))
    state = ""
    if request.POST:
        # print(dir(request.POST))
        usernm = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(username=usernm, password=passwd)
        if user is not None:
            if user.is_active:
                dj_login(request, user)
                state = "You're successfully logged in!"
                return redirect("/")
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    c["state"] = state
    c["user"] = request.user
    return render_to_response("login.html", c)


def logout(request):
    c = {}
    dj_logout(request)
    # c["user"] = request.user
    return redirect("/", c)
