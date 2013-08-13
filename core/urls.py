from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'core.views.login', name='login'),
    url(r'^accounts/logout/$', 'core.views.logout', name='logout'),
    url(r'^$', 'core.views.index', name='home'),
    url(r'^servermanager$', 'core.views.servermanager', name='Server Manager'),
    url(r'^saveserver$', 'core.views.saveserver')
)