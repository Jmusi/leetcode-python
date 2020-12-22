#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/14
# Solution: 求出每一层的高度，然后调用84题函数

class Solution:
    def maximalRectangle(self,matrix):
        if len(matrix)==0:
            return 0
        heights=[0]*len(matrix[0])
        maxArea=0
        for row in range(len(matrix)):
            #遍历每一列，更新高度
            for col in range(len(matrix[0])):
                if matrix[row][col]=='1':
                    heights[col]+=1
                else:
                    heights[col]=0

            maxArea=max(maxArea,self.largestRectangleArea(heights))
        return maxArea

    def largestRectangleArea(self,heights):
        #单调栈,固定高度
        n=len(heights)
        left,right=[0]*n,[0]*n
        mono_stack=list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]]>=heights[i]:
                mono_stack.pop()
            left[i]=mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack=list()
        for i in range(n-1,-1,-1):
            while mono_stack and heights[mono_stack[-1]]>=heights[i]:
                mono_stack.pop()
            right[i]=mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        ans = max((right[i]-left[i]-1)*heights[i] for i in range(n)) if n>0 else 0
        return ans

if __name__ == "__main__":
    s=Solution()
    print(s.maximalRectangle([["1","0","1","0","0"],
                              ["1","0","1","1","1"],
                              ["1","1","1","1","1"],
                              ["1","0","0","1","0"]]))
    pass 