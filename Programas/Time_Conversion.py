#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[8:] == 'PM':
        hora = int(s[:2]) + 12
        hora = hora if hora <= 23 else '12'
    else:
        hora = '00' if s[:2] == '12' else s[:2]
    
    return(f'{hora}{s[2:8]}')
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()