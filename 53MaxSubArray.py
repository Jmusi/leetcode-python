#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/30
# Solution:
class Solution:
    def maxSubArray(self,nums):
        #动态规划
        pre=0
        maxAns=nums[0]
        for x in nums:
            pre=max(pre+x,x) #当前位置的最大值=上一个位置的最大值+当前值，或者就是当前值
            maxAns=max(maxAns,pre)

        return maxAns
if __name__ == "__main__":
    s=Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    pass 