
import sys
import os
import pty
import time
import datetime
import subprocess as sp

from shutil import move
from hashlib import md5

import re
import subprocess

def is_running(process):
    s = subprocess.Popen(["ps", "axw"],stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            if '<defunct>' in x:
                return False
            else:
                return True
    return False

def run_pgDump(hostname, db, user, passwd):
    outfile = '.tmp.dump'
    ## pg_dump consumidores -U letmiapp_user -W -h localhost -f salida.dump
    pid, fd = pty.fork()
    if pid == pty.CHILD:
        os.execlp("pg_dump", "pg_dump", db,"-U", user, "-W", "-h", hostname, "-f", outfile)
    else:
        cn = os.read(fd, 1024)
        print(cn)
        os.write(fd, passwd + "\n")
        ctd = 0
        while ctd<120 and is_running(str(pid)):
            time.sleep(1)
            print('wait %i...'%(ctd))
            ctd += 1
        msj = os.read(fd, 1024)
        content = open(outfile).read()+str(datetime.datetime.now())
        nm = md5(content).hexdigest()+'.dump'
        move(outfile,os.sep.join(['postgres','media',nm]))
        return msj.strip()=='', msj, nm


if __name__ == '__main__':
    run_pgDump('salida.dump','consumidores','letmiapp_user','-A8c0Pd2jz?y')

