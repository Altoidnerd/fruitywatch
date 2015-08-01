#!/usr/bin/env python3

import sys
import math
from random import *

def convertColor(r,g,b):
    return 16 + (b%6) + 6*(g%6) + 36*(r%6)

def printColor(r,g,b,text):
    print("\[\\033[38;5;"+str(convertColor(r,g,b))+"m\]"+text,end="")

indexes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def colorizeStr(factor,string):
    r = math.floor(random()*len(indexes))
    print("\[\\033[1m\]",end="")
    for c in string:
        g = (r + 49) % len(indexes)
        b = (g + 49) % len(indexes)
        printColor(indexes[r],indexes[g],indexes[b],c)
        r = (r+factor) % len(indexes)

def main():
    colorizeStr(2, ' '.join(sys.argv[1:]))

if __name__ == '__main__':
    main()
