# Find a Peak Element II


from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        i=0
        j=len(mat[0])
        while i<=j:
            mid=(i+j)//2
            max_row=0
            for u in range(1,len(mat)):
                if mat[u][mid]>mat[max_row][mid]:
                    max_row=u
            
            is_left_smaller=mid-1<0 or mat[max_row][mid]>mat[max_row][mid-1]
            is_right_smaller=mid+1==len(mat[0]) or mat[max_row][mid]>mat[max_row][mid+1]
            if is_left_smaller and is_right_smaller:
                return [max_row,mid]
            if not is_left_smaller:
                j=mid-1
            else:
                i=mid+1
        return [-1,-1]
        