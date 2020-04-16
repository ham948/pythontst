#!/usr/bin/python3
from pathlib import Path
from svgwrt import *
start('hello',1000,1000)
print(coordconv(50,1000))
line(0,0,500,600)
rect(15,25,30,300)
end()
