#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSubarraysWithSumAndMaxAtMost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. LONG_INTEGER k
#  3. LONG_INTEGER M
#

def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    wins = 0
    if len(nums) == 0:
        return 0
    if (len(nums) == 1):
        if (nums[0] == k and nums[0] <= M):
            return 1
    mini = min(nums)
    for x in range(len(nums)):
        total = 0
        for y in range(x,len(nums)):
            item = nums[y]
            if (item > M or total + mini > k):
                break
            total += item
            if total == k:
                wins+=1
    # print(nums,k,M,wins)
    return wins

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    k = int(input().strip())

    M = int(input().strip())

    result = countSubarraysWithSumAndMaxAtMost(nums, k, M)

    print(result)
