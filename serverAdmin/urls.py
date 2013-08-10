from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serverAdmin.views.home', name='home'),
    #url(r'^serverAdmin/', include('serverAdmin.foo.urls')),

    url(r'^accounts/login/$', 'core.views.login', name='login'),
    url(r'^accounts/logout/$', 'core.views.logout', name='logout'),

    #################
    url(r'^pgbackup/?$', 'postgres.views.backup', name='PostgreSQL Backup'),
    url(r'^pgbackup/recover/(?P<num>\d+)/?$', 'postgres.views.restore_backup'),
    #################
    url(r'^$', 'core.views.index', name='home'),
    url(r'^servermanager$', 'core.views.servermanager', name='Server Manager'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
