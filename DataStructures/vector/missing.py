#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    new_list = []
    all_numbers = {}
    other_numbers = {}
    for i in brr:
        if all_numbers.get(i):
            all_numbers[i] += 1
        else:
            all_numbers[i] = 1
    
    for i in arr:
        if other_numbers.get(i):
            other_numbers[i] += 1
        else:
            other_numbers[i] = 1
    
    for i in all_numbers:
        if other_numbers.get(i) == None:
            new_list.append(i)
        elif other_numbers.get(i) != all_numbers.get(i):
            new_list.append(i)
        else:
            pass
            
    return sorted(new_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
