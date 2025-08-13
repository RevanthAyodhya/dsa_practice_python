# Max Consecutive Ones


from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        count=0
        for i in nums:
            if i==0:
                count=0
                
            else:
             
                count+=1
            if ans< count:
                ans=count
        
        return ans
        