#Missing Number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)
        for i in range(len(nums)):            
            res+=(i-nums[i])
        return res
        


# xor 
#sum of natural numbers formula