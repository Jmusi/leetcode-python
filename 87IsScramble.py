#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/14
# Solution:
class Solution:
    def isScramble(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        if s1==s2:
            return True
        if sorted(s1)!=sorted(s2):
            return False
        for i in range(1,len(s1)):
            #有两种类型，交换或者不交换
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]) or \
                    (self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i])):
                return True
        return False
    def isScrambleV2(self,s1,s2):
        #动态规划
        #dp[i][j][len]dp[i][j][len] 表示从字符串 S 中 i 开始长度为 len 的字符串是否能变换为从字符串 T 中 j 开始长度为 len
        # 的字符串，所以答案是 dp[0][0][n]。 时间复杂度 O(N^4)，空间复杂度O(N^3)

        if len(s1)!=len(s2):
            return False
        n=len(s1)
        dp=[[[False for _ in range(n+1)] for _ in range(n)] for _ in range(n)]
        #单个字符
        for i in range(n):
            for j in range(n):
                dp[i][j][1]=(s1[i]==s2[j])
        #长度在2-n
        for lens in range(2,n+1):
            #枚举s1起点位置
            for i in range(n-lens+1):
                #枚举s2起点
                for j in range(n-lens+1):
                    #枚举划分位置
                    for k in range(1,lens):
                        if dp[i][j][k] and dp[i+k][j+k][lens-k]:
                            dp[i][j][lens]=True
                            break
                        if dp[i][j+lens-k][k] and dp[i+k][j][lens-k]:
                            dp[i][j][lens]=True
                            break
        return dp[0][0][n]

if __name__ == "__main__":
    s=Solution()
    print(s.isScrambleV2('great','grate'))
    pass 