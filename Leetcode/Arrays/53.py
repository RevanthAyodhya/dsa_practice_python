# Maximum Subarray
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        count=0
        for i in nums:
            if count<0:
                count=0
            count+=i
            max_sum= count if count>max_sum else max_sum
        return max_sum