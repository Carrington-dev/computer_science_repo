#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    if len(arr) == 1:
        return "YES"
    for i in range(len(arr)):
        print(arr[:i], arr[i+1:])
        if sum(arr[:i]) == sum(arr[i+1:]):
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

# ALL TEST CASES PASSED

def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0

    for num in arr:
        if left_sum == (total_sum - left_sum - num):
            return "YES"
        left_sum += num

    return "NO"