# Minimum Number of Days to Make m Bouquets

from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l,r=1,max(bloomDay)
        res=-1
        while l<=r:
            mid=(l+r)//2
            consecutive_length,bouq=0,0
            for flower in bloomDay:
                if flower<=mid:
                    consecutive_length+=1
                    if consecutive_length>=k:
                        consecutive_length=0
                        bouq+=1
                else:
                    consecutive_length=0 
            if bouq>=m:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        