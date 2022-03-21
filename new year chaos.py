#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    total_bribe = 0
    len_of_q_to_be_considered = len(q)
    swaped = False
    
    #Chaotic checking
    for i in range(len(q)):
        #Since the smallest value of the array is always 1
        if q[i]-1-i > 2:
            print('Too chaotic')
            return
    #bubble Sorting to get the total number of bribes
    for i in range(len_of_q_to_be_considered):
        for j in range(len_of_q_to_be_considered):
            if j+1 != len(q) and q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                total_bribe += 1
                swaped = True
        if swaped:
            swaped = False
        else: 
            break
        
        len_of_q_to_be_considered -= 1
        
    print(total_bribe)
                   

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
