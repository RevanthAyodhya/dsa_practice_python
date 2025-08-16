# Majority Element

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        i=0
        n=len(nums)
        ans=-1
        for i in range(n):    #improve for loop
            if count==0:
                ans=nums[i]
                count+=1
            elif nums[i]==ans:
                count+=1
            else:
                count-=1
       
        count=0
        i=0
        for i in range(n):
            if nums[i]==ans:
                count+=1
           
        if count>n//2:
            return ans
    
        

    
    # Brute force ---- Using HashMap 