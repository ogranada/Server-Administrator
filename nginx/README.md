DEPLOY
======

This folder and content are based on [wsgi Django's documentation](https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html).
The serveradmin.conf file will be copied to /etc/nginx/sites-available:
* copy serveradmin.conf /etc/nginx/sites-available/
and will make a link to this file in /etc/nginx/sites-enabled/ with:
* cd /etc/nginx/sites-enabled/
* ln -s /etc/nginx/sites-available/serveradmin.conf
Move serverAdminWsgi.py and runWSGI.sh to parent folder
* move ./serverAdminWsgi.py ..
Later you will run the runWSGI.sh file:
* sh runWSGI.sh


