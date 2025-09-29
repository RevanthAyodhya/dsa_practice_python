
# Valid Anagram

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpp1,mpp2={},{}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            mpp1[s[i]]=1 + mpp1.get(s[i],0)
            mpp2[t[i]]=1+mpp2.get(t[i],0)
   
            
        
        for c in s:
            if mpp1[c]!=mpp2.get(c,0):
                return False
        return True

        


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
     

        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
     

        