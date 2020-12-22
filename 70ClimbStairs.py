#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/1
# Solution: 斐波那契数列，有数学上的计算公式

class Solution:
    def climbStairs(self,n):
        if n==1:
            return 1
        dp=[0]*n
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]


if __name__ == "__main__":
    s=Solution()
    print(s.climbStairs(7))
    pass 