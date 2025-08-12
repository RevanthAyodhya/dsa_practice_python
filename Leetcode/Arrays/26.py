# Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        pos=1
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):        #sliding window
                nums[pos]=nums[i]
                pos+=1
        return pos