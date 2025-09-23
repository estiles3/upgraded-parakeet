#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    if (len(intervals) < 1):
        return intervals
    intervals.sort(key=lambda x:x[0])
    newlist = [intervals[0]]
    for x in range(1,len(intervals)):
        if (newlist[-1][1] >= intervals[x][0]):
            if (newlist[-1][1] < intervals[x][1]):
                newlist[-1][1] = intervals[x][1]
        else:
            newlist.append(intervals[x])
    return newlist

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
