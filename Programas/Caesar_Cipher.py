#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    n = 26
    message = ''
    
    for letter in s:
        new_letter = letter
        for i in range(n):
            if letter == alphabet_lower[i]:
                new_letter = alphabet_lower[(i + k) % n]
                break
            if letter == alphabet_upper[i]:
                new_letter = alphabet_upper[(i + k) % n]
                break
        message += new_letter
    return message

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
