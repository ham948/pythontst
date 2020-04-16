#!/usr/bin/python3

from pathlib import Path
block=[]
atribs={}
parts={}
gerb= open('copper_top.gbr','r')
gerbwhole = gerb.read()
gerblin = gerbwhole.split('\n')
del gerblin[-1]
for i in range(len(gerblin)):
    if gerblin[i]=='':
        continue
    elif gerblin[i][0]=='%':
        if gerblin[i][1:6]=='FSLAX':
            global units,decimals
            units = int(gerblin[i][6])
            decimals = int(gerblin[i][7])
        if gerblin[i][1:3]=='MO':
            'enter mm or inch conversion stuff here'
        if gerblin[i][1:3]=='AD':
            if gerblin[i][6]=='C':
                atribs[gerblin[i][3:6]]=['C',float(gerblin[i][8:9+units+decimals])]
            if gerblin[i][6]=='R':
                atribs[gerblin[i][3:6]]=['R',float(gerblin[i][8:9+units+decimals]),float(gerblin[i][10+units+decimals:11+2*(units+decimals)])]
                print(atribs[gerblin[i][3:6]])
    elif gerblin[i][0]=='D':
        j=i+1
        block=[gerblin[i][0:3]]
        while gerblin[j][0]=='X':
            print(gerblin[j][0],j)
            print(gerblin[i][0:3])
            j+=1
    else:
        continue

print(f'hello:{units} and : {decimals}')
print(list(atribs.keys())[0])
print(block)
