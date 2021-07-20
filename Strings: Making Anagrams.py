#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a_dic = {}
    b_dic = {}
    
    for letter in a:
        if letter in a_dic.keys():
            a_dic[letter] += 1
        else:
            a_dic[letter] = 1
            
    for letter in b:
        if letter in b_dic.keys():
            b_dic[letter] += 1
        else:
            b_dic[letter] = 1
    num_of_deletions = 0
    for key in a_dic.keys():
        if key not in b_dic.keys():
            num_of_deletions += a_dic[key]
        else:
            if a_dic[key] == b_dic[key]:
                continue
            else:
                num_of_deletions += abs(a_dic[key] - b_dic[key])
            
    for key in b_dic.keys():
        if key not in a_dic.keys():
            num_of_deletions += b_dic[key]
            
    return num_of_deletions
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
