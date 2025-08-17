#  Next Permutation
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        index=-1
        i=n-2
        while(i>=0):
            if nums[i]<nums[i+1]:
                index=i
                break
            i-=1
        if index==-1:
            nums.reverse()
        else:
            k=n-1
            while k>index:
                if nums[k]>nums[index]:
                    nums[k],nums[index]=nums[index],nums[k]
                    break
                k-=1
            nums[index+1:]=reversed(nums[index+1:])
            
        