#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    if len(responseTimes) < 2:
        return 0
    start = [responseTimes[0]]
    # print(responseTimes)
    count = 0
    for x in range(1,len(responseTimes)):
        avg = sum(start) / len(start)
        if (avg <responseTimes[x]):
            count +=1
        start.append(responseTimes[x])
    return(count)

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
