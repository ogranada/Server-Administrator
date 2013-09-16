DEPLOY
======

This folder and content are based on [uwsgi Django's documentation](https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html).

The serveradmin.conf file will be copied to /etc/nginx/sites-available:
* `cp serveradmin.conf /etc/nginx/sites-available/`

later you will make a link to this file in /etc/nginx/sites-enabled/ with:
* `cd /etc/nginx/sites-enabled/`
* `ln -s /etc/nginx/sites-available/serveradmin.conf`

Finally move serverAdminWsgi.py and runWSGI.sh to parent folder and run the runWSGI.sh file:
* `mv ./serverAdminWsgi.py ..`
* `sh runWSGI.sh`


