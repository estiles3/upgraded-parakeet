#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    orderNumbers.sort()
    count = 1
    previous = 1
    if(len(orderNumbers) < 1):
        return 1
    for x in range(len(orderNumbers)):
        num = orderNumbers[x]
        # print(num,count,num==count)
        if (num >0):
            if(num == count):
                previous= count
                count += 1
            elif (num == previous):
                continue
            else:
                return(count)
    return(count)

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
