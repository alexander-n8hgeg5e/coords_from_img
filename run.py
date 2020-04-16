#!/usr/bin/env python3
# coding: utf-8
from subprocess import Popen,PIPE
from signal import signal,SIGINT,default_int_handler,SIGTERM
from time import sleep
filename="plot_start"

popen=Popen(['gnuplot',filename,"-"],stderr=PIPE,restore_signals=False)
data=b""

def handle_int(a,b):
    popen.send_signal(SIGINT)
    popen.send_signal(SIGTERM)

signal(SIGINT,handle_int)
data=popen.stderr.read()
signal(SIGINT,default_int_handler)
data=data.split(b"\n")
_data=data
data=[]
for d in _data:
    dd=d.strip()
    if len(dd) > 0 :
        try:
            data.append(tuple(round(float(j),3) for j in dd.split(b" ")))
        except ValueError:
            print(dd)

with open('coords.data','wt') as f:
    f.write(repr(data))

for i,j in data:
    print(i,j)


#b=[]
#for p in a:
#    b.append(tuple(round(float(f),3) for f in p.split(" ")))
#    
    
