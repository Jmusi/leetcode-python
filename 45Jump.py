#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/27
# Solution:
class Solution:
    def jump(self,nums):
        #贪心
        n=len(nums)
        maxPos,end,step=0,0,0
        # 对于数组 [2,3,1,2,4,2,3]，初始位置是下标 0，从下标 0 出发，最远可到达下标 2。
        # 下标 0 可到达的位置中，下标 1 的值是 3，从下标 1 出发可以达到更远的位置，因此第一步到达下标 1
        for i in range(n-1):
            if maxPos>=i:
                maxPos=max(maxPos,i+nums[i])
                if i==end:
                    #表示已经到底上一个开始位置的最远能到达位置
                    end=maxPos
                    step+=1
        return step


if __name__ == "__main__":
    s=Solution()
    print(s.jump([2,3,1,2,4,2,3]))
    pass 