#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/4
# Solution:
class Solution:
    def searchMatrix(self,matrix,target):
        if matrix==[]:
            return False
        left=0
        m=len(matrix)
        n=len(matrix[0])
        right=m*n-1
        while left<=right:
            mid=(left+right)//2
            x=mid//n
            y=mid%n
            if matrix[x][y]==target:
                return True
            if matrix[x][y]<target:
                left=mid+1
            else:
                right=mid-1
        return False
if __name__ == "__main__":
    s=Solution()
    print(s.searchMatrix([[1,1]],2))
    pass 