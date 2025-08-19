# Majority Element II


from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1,cnt2=0,0
        el1,el2=None,None
        ans=[]
        n=len(nums)
        for i in nums:
            if cnt1==0 and el2!=i:
                cnt1+=1
                el1=i
            elif cnt2==0 and el1!=i:
                cnt2+=1
                el2=i
            elif el1==i:
                cnt1+=1
            elif el2==i:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
            
        cnt1,cnt2=0,0
        for i in nums:
            if el1==i:
                cnt1+=1
            if el2==i:
                cnt2+=1
        if cnt1>(n//3):
            ans.append(el1)
        if cnt2>(n//3):
            ans.append(el2)
        
        return ans