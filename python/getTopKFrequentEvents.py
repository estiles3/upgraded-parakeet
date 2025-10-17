#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTopKFrequentEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY events
#  2. INTEGER k
#

def getTopKFrequentEvents(events, k):
    # Write your code here
    ourdict = {}
    # print(events)
    for x in events:
        if (x in ourdict):
            ourdict[x] += 1
        else:
            ourdict[x] = 1
    highest= []
    for x in ourdict:
        highest.append([x,ourdict[x]])
    highest.sort(key=lambda x:x[1], reverse=True)
    outputlist = []
    for x in range(k):
        outputlist.append(highest[x][0])
    
    return outputlist

if __name__ == '__main__':
    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    k = int(input().strip())

    result = getTopKFrequentEvents(events, k)

    print('\n'.join(map(str, result)))
