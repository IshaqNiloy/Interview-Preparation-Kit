#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    previous = 0
    counter = k
    
    for price in c:
        if counter > 0:
            cost += (previous + 1) * price
            counter -= 1
        else:
            previous += 1
            counter = k 
            cost += (previous + 1) * price
            counter -= 1
    
    return cost
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
