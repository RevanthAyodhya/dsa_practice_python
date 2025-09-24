# Longest Common Prefix
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first_word=strs[0]
        last_word=strs[len(strs)-1]
        n=len(first_word)
        res=''
        for i in range(0,n):
            if first_word[i]==last_word[i]:
                res+=first_word[i]
            else:
                break
        return res
   
        