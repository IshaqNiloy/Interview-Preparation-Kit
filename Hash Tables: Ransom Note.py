#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    magazine_dic = {}
    note_dic = {}
    
    for word in magazine:
        if word in magazine_dic.keys():
             magazine_dic[word] += 1
        else:
            magazine_dic[word] = 1
            
    for word in note:      
        if word in note_dic.keys():
             note_dic[word] += 1
        else:
            note_dic[word] = 1
        
    for key in note_dic.keys():
        if key in magazine_dic.keys() and magazine_dic[key] >= note_dic[key] :
            continue
        else:
            print('No')
            return
        
    print('Yes')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
