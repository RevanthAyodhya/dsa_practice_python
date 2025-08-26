# Find First and Last Position of Element in Sorted Array

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binary(nums,target,True)
        right=self.binary(nums,target,False)
        return[left,right]
    
    def binary(self,nums,target,bias):
        left=0
        right=len(nums)-1
        i=-1
        while left<=right:
            m=(left+right)//2
            if target>nums[m]:
                left=m+1
            elif target<nums[m]:
                right=m-1
            else:
                i=m
                if bias:
                    right=m-1
                else:
                    left=m+1
        return i
        