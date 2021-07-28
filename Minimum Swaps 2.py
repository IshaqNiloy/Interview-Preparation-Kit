#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    min_swaps = 0
    temp = 0
    i = 0
    
    while i < len(arr):
        if arr[i] == i+1:
            i += 1
            continue
        else:
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            min_swaps += 1
            #We are selecting a specific location and validating whether the value belongs to that location or not. If not then we are placing the value to its correct position. More specifically we are swaping the values. After swaping one value goes to its correct position. For another value we have to recheck whether that value belongs to that posittion or not.
            i -= 1
        i += 1
            
    
    return min_swaps
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
