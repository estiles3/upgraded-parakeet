#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findLongestArithmeticProgression' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findLongestArithmeticProgression(arr, k):
    # Write your code here
    total = 0
    if len(arr) < 2:
        return len(arr)
    arr.sort()
    newlist = []
    for x in arr:
        if x not in newlist:
            newlist.append(x)
    arr = newlist
    prev = {}
    # print(arr)
    for x in range(len(arr)):
        checked = False
        ourlist = [arr[x]]
        if (len(arr[x:]) <= total):
            break
        if (arr[x] in prev):
            # print(prev)
            continue
        for y in range(x,len(arr)):
            maxi = ourlist[-1]
            # print(arr[y], maxi+ k)
            # print(ourlist)
            if arr[y]  == maxi+ k:
                ourlist.append(arr[y])
            elif arr[y]  > maxi+ k:
                if total < len(ourlist):
                    total = len(ourlist)
                for z in ourlist:
                    prev[z] = 1
                    checked = True
                # print(prev)
                break
        if not checked:
            for z in ourlist:
                prev[z] = 1
            if total < len(ourlist):
                total = len(ourlist)
    if total < len(ourlist):
        total = len(ourlist)
    return total

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findLongestArithmeticProgression(arr, k)

    print(result)
