def pairs(k, arr):
    # Convert the list to a set for O(1) lookups
    arr_set = set(arr)
    count = 0
    
    # Check for each element if there's a pair with difference k
    for x in arr:
        if x + k in arr_set:
            count += 1
        if x - k in arr_set:
            count += 1
    
    # Since each pair is counted twice, we return half the count
    return count // 2


# My solution but not efficient
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    nums = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if abs(arr[i] - arr[j]) == k:
                nums.add(tuple(sorted((arr[i], arr[j]))))
    return len(nums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
