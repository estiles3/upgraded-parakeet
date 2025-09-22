class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        wins = 0
        for x in range(len(nums)):
            if (nums[x] <= right):
                check = left <= nums[x] <= right
                for y in range(x,len(nums)):
                    if nums[y] > right:
                        break
                    if check:
                        wins += 1
                        continue
                    if(not check):
                        check = left <= nums[y] <= right
                        if check:
                            wins += 1
                    
        return wins
        