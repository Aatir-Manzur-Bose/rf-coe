import subprocess

subprocess.call('python dropout.py', creationflags=subprocess.CREATE_NEW_CONSOLE,shell=True)
subprocess.call('python RFLatency.py',creationflags=subprocess.CREATE_NEW_CONSOLE,shell=True)
subprocess.call('python ldausbcli_007.py -i 8333 -a 0 -f 1 -s 60 -e 20 -w 350 -d 10 -o 0 -k 2 -p 2 -M 1 -b 350 -B 1',creationflags=subprocess.CREATE_NEW_CONSOLE,shell=True)