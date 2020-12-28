#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/12/28
# Solution:
'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。
'''

def maxArea(height):
    left=0
    right=len(height)-1
    maxarea=0
    while left<right:
        area=min(height[left],height[right])*(right-left)
        maxarea=max(maxarea,area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return maxarea

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))
    pass 