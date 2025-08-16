# Best Time to Buy and Sell Stock
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r=0,1
        p=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                p=max(p,profit)
            else:
                l=r
            r+=1
        return p
        