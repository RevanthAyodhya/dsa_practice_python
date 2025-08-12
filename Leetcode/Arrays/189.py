# Rotate Array

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        self.revers(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
    
    def reverse(self,nums:List[int],l:int,r:int)->None:
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1
        


# Brute force:
# Take an array and copy the element one by one with i+k 
# we get out of bounds error for last elements
# we can use (i+k)%n to store the element in exact position