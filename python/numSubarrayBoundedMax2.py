class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        wins = 0
        value = 0
        previous = 0
        localmax = 0
        for x in range(len(nums)):
            if localmax < left:
                localmax = nums[x]
            if nums[x] < left:
                value+=1
            elif (nums[x] > right):
                previous = x+1
                localmax = 0
                value = 0
            else:
                value = 0
            if (left <= localmax <= right):
                wins += x+ 1 -previous  - value
        return wins
        