#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/31
# Solution:
class Solutin:
    def canJump(self,nums):
        n=len(nums)
        right_most=0 #记录当前能到达的最优位置
        for i in range(n):
            if i<=right_most:
                right_most=max(i+nums[i],right_most)
                if right_most>=n-1:
                    return True
        return False

if __name__ == "__main__":
    s=Solutin()
    print(s.canJump([2,3,1,1,4]))
    pass 