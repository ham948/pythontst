#!/usr/bin/python3

import random, time, copy
WIDTH = 80
HEIGHT = 40

#create list of cells
nextcell = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if (random.randint(0,1) == 0):
            column.append('#')
        else:
            column.append(' ')
    nextcell.append(column)

while True:
    print("\n\n")
    currentcell= copy.deepcopy(nextcell)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentcell[x][y],end='')
        print() #newline at end of row

    for x in range(WIDTH):
        for y in range(HEIGHT):

            lcoord= (x-1)%WIDTH
            rcoord= (x+1)%WIDTH
            acoord= (y+1)%HEIGHT
            bcoord= (y-1)%HEIGHT

            numnb = 0
            if currentcell[lcoord][acoord] == '#':
                numnb += 1
            if currentcell[x][acoord] == '#':
                numnb += 1
            if currentcell[rcoord][acoord] == '#':
                numnb += 1
            if currentcell[lcoord][y] == '#':
                numnb += 1
            if currentcell[rcoord][y] == '#':
                numnb += 1
            if currentcell[lcoord][bcoord] == '#':
                numnb += 1
            if currentcell[x][bcoord] == '#':
                numnb += 1
            if currentcell[rcoord][bcoord] == '#':
                numnb += 1

            if currentcell[x][y] == '#' and (numnb==2 or numnb==3):
                nextcell[x][y]= '#'
            elif currentcell[x][y] == ' ' and (numnb==3):
                nextcell[x][y] = '#'
            else:
                nextcell[x][y] = ' '
        time.sleep(0.001)
