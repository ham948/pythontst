#!/usr/bin/python3

from pathlib import Path
import shelve
def coordconv(x,y):
    y=ysize-y
    return(x,y)
def line(x1,y1,x2,y2):
    x1,y1=coordconv(x1,y1)
    x2,y2=coordconv(x2,y2)
    dfile.write(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black"/>\n')

def circle(x,y,r):
    x,y=coordconv(x,y)
    dfile.write(f'<circle cx="{x}" cy="{y}" r="{r}" stroke="black"/>\n')
def rect(x,y,w,h):
    x,y=coordconv(x,y)
    dfile.write(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke="black"/>\n')
def start(name,x,y):
    global dfile
    global xsize
    global ysize
    xsize =x
    ysize =y
    currentDir = Path.cwd()/Path(name+'.svg')
    if currentDir.exists():
        tmp= open(currentDir,'r').readlines()
        dfile = open(currentDir,'w')
        del tmp[-1]
        for i in tmp:
            dfile.write(i)
        dfile.close()
        dfile = open(currentDir,'a')

    if  not currentDir.exists():
        dfile = open(currentDir,'a')
        dfile.write(f'<svg height="{y}" width="{x}">\n<rect width="100%" height="100%" fill="white"/>\n')

'''
start('drawii')
line(0,0,50,50)
circle(25,25,10)
rect(10,10,20,20)
'''
def end():
    dfile.write('\n\n</svg>')
    dfile.close()
