# Maximum Product Subarray


from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin,curMax=1,1
        for i in nums:
            if i==0:
                curMin,curMax=1,1
                continue

            temp=i*curMax
            curMax=max(temp,i*curMin,i)
            curMin=min(temp,i*curMin,i)
            res=max(res,curMax)
        return res
        
        