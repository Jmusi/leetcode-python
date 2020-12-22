#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/12
# Solution:固定长或者宽，其中一个变量
class Solution:
    def largestRectangleArea(self,heights):
        #暴力解法，固定宽为(right-left+1),寻找高度(即区间内的最小值，才能组成矩形),
        ans=0
        for left in range(len(heights)):
            minHeight=None
            for right in range(left,len(heights)):
                minHeight=min(minHeight,heights[right]) if minHeight!=None else heights[right]
                #计算面积
                ans=max(ans,(right-left+1)*minHeight)
        return ans
    def largestRectangleAreaV2(self,heights):
        #固定高度，向两侧延申，寻找最大宽度，即不小于当前高度的区间。
        ans=0
        for mid in range(0,len(heights)):
            height=heights[mid]
            left=mid
            right=mid
            #确定左边界
            while left-1>=0 and heights[left-1]>=height:
                left-=1
            #确定右边界
            while right+1<len(heights) and heights[right+1]>=height:
                right+=1
            ans=max(ans,(right-left+1)*height)
        return ans
    def largestRectangleAreaV3(self,heights):
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
    print(s.largestRectangleAreaV3([2,1,5,6,2,3]))
    pass 