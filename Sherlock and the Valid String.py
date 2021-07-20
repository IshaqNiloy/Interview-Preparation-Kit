#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    letter_dic = {}
    
    for letter in s:
        if letter in letter_dic.keys():
            letter_dic[letter] += 1
        else:
            letter_dic[letter] = 1
            
    if len(set(letter_dic.values()))==1 or len(set(sorted(list(letter_dic.values()))[1:])) == 1:
        return 'YES'
    else:
        for value in sorted(list(letter_dic.values()))[:-1]:
            if value == max(letter_dic.values()) - 1:
                continue
            else:
                return 'NO'    
        return 'YES' 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
