#Subarray Sum Equals K 

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res=0
        count=0
        pre_sum={0:1}
        for i in nums:
            count+=i
            diff=count-k
            res+=pre_sum.get(diff,0)
            pre_sum[count]=1+pre_sum.get(count,0)
        return res
        
        