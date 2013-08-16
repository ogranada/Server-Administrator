#!/bin/bash

uwsgi --socket :8001 --wsgi-file serverAdminWsgi.py -d true


