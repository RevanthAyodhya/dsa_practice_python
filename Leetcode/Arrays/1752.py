# Check if Array Is Sorted and Rotated

class Solution(object):
    def check(self, nums):
        n=len(nums)
        if n==1:
            return True
        count =1
        for i in range(1,2*n):
            if(nums[(i-1)%n])<nums[i%n]:     # i%n prevents using the extra space
                count+=1
            else:
                count-=1
            if count==n:
                return True
        return False
