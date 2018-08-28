##子进程

import subprocess
from datetime import datetime


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


if __name__ == '__main__':
    start = datetime.now()
    procs = []
    for _ in range(10):
        proc = run_sleep(0.1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()

    end = datetime.now()
    time = (end - start).total_seconds()
    print('Finished in %.3f seconds' % time)
