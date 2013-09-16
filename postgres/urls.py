from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^pgbackup/?$', 'postgres.views.backup', name='PostgreSQL Backup'),
    url(r'^databases/?$', 'postgres.views.databases', name='Bases de Datos'),
    url(r'^pgbackup/recover/(?P<num>\d+)/?$', 'postgres.views.restore_backup'),
    url(r'^pgbackup/download/(?P<num>\d+)/?$', 'postgres.views.download_file'),
    url(r'^savedatabase/?$', 'postgres.views.savedatabase'),
    url(r'^savebackup/?$', 'postgres.views.savebackup')
)
