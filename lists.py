#!/usr/bin/python3

catnames = []

while True:
    print("enter the name of cat"+str(len(catnames)+1)+" or enter nothing to stop.:")
    name = input()
    if name == '':
        break
    catnames= catnames + [name]
print("the cat names are:")
for name in catnames:
    print("  "+name)
