#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    less_than_zero = 0
    equals_zero = 0
    greater_than_zero = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            less_than_zero += 1
        elif arr[i] == 0:
            equals_zero += 1
        else:
            greater_than_zero += 1
    print("{:.6f}".format(greater_than_zero/len(arr)))
    print("{:.6f}".format(less_than_zero/len(arr)))
    print("{:.6f}".format(equals_zero/len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
