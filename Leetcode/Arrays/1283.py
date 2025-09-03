# Find the Smallest Divisor Given a Threshold

from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r=1,max(nums)
        res=None
        while l<=r:
            count=0
            mid=l+(r-l)//2
            for i in nums:
                count+=math.ceil(i/mid)
            if count<=threshold:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res

        