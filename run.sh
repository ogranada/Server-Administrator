#!/bin/bash
python -B manage.py compilemessages
python -B manage.py syncdb
python -B manage.py runserver 0.0.0.0:9090 




