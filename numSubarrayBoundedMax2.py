class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        wins = 0
        value = 0
        previous = 0
        localmax = 0
        for x in range(len(nums)):
            if nums[x] < left:
                value+=1
            if localmax < left:
                localmax = nums[x]
            if (nums[x] > right):
                previous = x+1
                localmax = 0
                value = 0
            if left <= nums[x] <= right:
                value = 0
            if (left <= localmax <= right):
                wins += len(nums[previous:x+1]) - value
        return wins
        