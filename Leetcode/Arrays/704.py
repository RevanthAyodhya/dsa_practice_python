# Binary Search

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        return self.binary(nums,target,0,n-1)
    

    def binary(self,nums,k,left,right)-> int:
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==k:
                return mid
            elif nums[mid]<k:
                left=mid+1
            else:
                right=mid-1
        return -1
    



    
        