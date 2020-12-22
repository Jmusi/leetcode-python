#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/31
# Solution: 动态规划
import math
class Solution:
    def uniquePaths(self,m,n):
        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))
    def uniquePathsV2(self,m,n):
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #dp表示到达i,j的最多路径,边界值都是1
        dp=[[1]*n]+[[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

    def uniquePathsV3(self,m,n):
        #优化空间复杂度O(n)，只记录上一行的数据
        cur=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j]+=cur[j-1]
        return cur[-1]
if __name__ == "__main__":
    s=Solution()
    print(s.uniquePaths(3,2))
    pass 