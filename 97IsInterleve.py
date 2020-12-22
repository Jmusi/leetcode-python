#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/19
# Solution: 动态规划，子问题为dp[i][j]:s1前i个字符和s2前j个字符能否构成s3前i+j个字符

class Solution:
    def isInterleve(self,s1,s2,s3):
        x,y,z=len(s1),len(s2),len(s3)
        if x+y!=z:
            return False
        dp=[[False]*(y+1) for i in range(x+1)]
        dp[0][0]=True
        for i in range(1,x+1):
            dp[i][0]=(dp[i-1][0] and s1[i-1]==s3[i-1])
        for i in range(1,y+1):
            dp[0][i]=(dp[0][i-1] and s2[i-1]==s3[i-1])
        for i in range(1,x+1):
            for j in range(1,y+1):
                dp[i][j]=(dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]
if __name__ == "__main__":
    s=Solution()
    print(s.isInterleve('aabcc','dbbca','aadbbcabcc'))
    pass 