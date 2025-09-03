# Capacity To Ship Packages Within D Days



from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def canShip(cap):
            ship,currCap=1,cap
            for w in weights:
                if currCap-w<0:
                    ship+=1
                    currCap=cap
                currCap-=w
            return ship<=days

        while l<=r:
            cap=(l+r)//2
            if canShip(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res
            
        