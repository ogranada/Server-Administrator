
import sys
import os
import pty
import time

def run_pgDump(outfile, hostname, db, user, passwd):
    ## pg_dump consumidores -U letmiapp_user -W -h localhost -f salida.dump
    pid, fd = pty.fork()
    if pid == pty.CHILD:
        os.execlp("pg_dump", "pg_dump", db,"-U", user, "-W", "-h", hostname, "-f", outfile)
    else:
        os.read(fd, 1024)
        os.write(fd, passwd + "\n")
        time.sleep(5)
        msj = os.read(fd, 1024)
        print msj
        return msj.strip()=='', msj


if __name__ == '__main__':
    run_pgDump('salida.dump','consumidores','letmiapp_user','-A8c0Pd2jz?y')

