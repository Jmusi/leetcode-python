#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/26
# Solution:
class Solution:
    def trap(self,height):
        sum=0
        # V1:求每一列的水，我们只需要关注当前列，以及左边最高的墙，右边最高的墙就够了
        for i in range(len(height)-1):
            max_left=0
            for j in range(i-1,-1,-1):
                if height[j]>max_left:
                    max_left=height[j]
            max_right=0
            for j in range(i+1,len(height)):
                if height[j]>max_right:
                    max_right=height[j]
            # 找出两端较小值
            minv=min(max_right,max_left)
            if minv>height[i]:
                sum+=(minv-height[i])
        return sum

    def trapV2(self,height):
        # V2：动态规划
        sum=0
        max_left=[0 for _ in range(len(height))] #状态，记录i位置的左边最大值
        max_right=[0 for _ in range(len(height))] # 记录i位置的右边最大值
        for i in range(1,len(height)-1):
            max_left[i]=max(max_left[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            max_right[i]=max(max_right[i+1],height[i+1])

        for i in range(1,len(height)-1):
            minv=min(max_left[i],max_right[i])
            if minv>height[i]:
                sum+=(minv-height[i])
        return sum
    def trapV3(self,height):
        #双指针
        sum=0
        max_left=0
        max_right=0
        left=1 #左指针
        right=len(height)-2 #右指针
        for i in range(1,len(height)-1):
            #从左到右跟新
            if height[left-1]<height[right+1]:
                max_left=max(max_left,height[left-1])
                minv=max_left
                if minv>height[left]:
                    sum+=(minv-height[left])
                left+=1
            else:
            #从右到左更新
                max_right=max(max_right,height[right+1])
                minv=max_right
                if minv>height[right]:
                    sum+=(minv-height[right])
                right-=1
        return sum
if __name__ == "__main__":
    s=Solution()
    print(s.trapV3([0,1,0,2,1,0,1,3,2,1,2,1]))
    pass 