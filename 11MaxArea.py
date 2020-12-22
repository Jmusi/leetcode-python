#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/19
# Solution:

class Solution:
    def maxArea(self,height):
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            max_area=max(area,max_area)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_area


if __name__ == "__main__":
    s=Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    pass 