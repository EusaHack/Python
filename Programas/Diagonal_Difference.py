#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    list_1 = []
    list_2 = []
    for i, sublist in enumerate(arr):
        valor = sublist[i]
        list_1.append(valor)
    for i, sublist in enumerate(arr):
        valor = sublist[-i -1]
        list_2.append(valor)
    
    return abs(sum(list_1) - sum(list_2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
