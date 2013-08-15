
import sys
import os
import pty
import time
import subprocess as sp



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

def run_pgDump(outfile, hostname, db, user, passwd):
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
        return msj.strip()=='', msj


if __name__ == '__main__':
    run_pgDump('salida.dump','consumidores','letmiapp_user','-A8c0Pd2jz?y')

