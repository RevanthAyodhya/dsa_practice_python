# Search a 2D Matrix

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        top,bot=0,row-1
        while top<=bot:
            mid=(top+bot)//2
            if target > matrix[mid][-1]:
                top=mid+1
            elif target< matrix[mid][0]:
                bot=mid-1
            else:
                break
        if not (top<=bot):
            return False
        l,r=0,col-1
        fixed_row=(top+bot)//2
        while l<=r:
            mid=(l+r)//2
            if target>matrix[fixed_row][mid]:
                l=mid+1
            elif target<matrix[fixed_row][mid]:
                r=mid-1
            else:
                return True
        return False