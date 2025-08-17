#  Rearrange Array Elements by Sign

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        j,k=0,1
        ans=[0]*n
        for i in nums:
            if i >= 0:
                ans[j]=i
                j+=2
            else:
                ans[k]=i
                k+=2
        return ans
        

      