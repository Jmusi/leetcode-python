''#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/27
# Solution: 实现一个支持 '?' 和 '*' 的通配符匹配
class Solution:
    def isMatch(self,s,p):
        #动态规划
        #dp[i][j]表示s截止到第i个位置(s[i - 1])的子串与p截止到第j个位置(p[j - 1])的子串是否匹配
        dp=[[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0]=True #空字符串匹配
        #对空s对应的匹配状态初始化
        for j in range(1,len(p)+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-1]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                # // 根据模式串的当前位置的字符来分类讨论,
                # 当前位置是 *, * 可以匹配任意字符包括空字符，所以考虑
                # dp[i-1][j-1],dp[i-1][j],dp[i][j-1]这前面已处理过的三个结果
                #但其实 dp[i-1][j-1]不用考虑，因为考虑dp[i-1][j]时也会执行这个if，还是会考虑到dp[i-1][j-1]

                if p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                elif p[j-1]=='?' or s[i-1]==p[j-1]:
                    dp[i][j]=dp[i-1][j-1]

        return dp[len(s)][len(p)]

if __name__ == "__main__":
    s=Solution()
    print(s.isMatch('adceb','*a*b'))
    pass 