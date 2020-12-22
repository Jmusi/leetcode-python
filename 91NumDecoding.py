#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/15
# Solution:
class Solution:
    def numDecoding(self,s):
        if s[0]=='0':
            return 0
        pre,curr=1,1
        #动态规划
        for i in range(1,len(s)):
            tmp=curr
            if s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    curr=pre
                else:
                    return 0
            elif s[i-1]=='1' or (s[i-1]=='2' and s[i]>='1' and s[i]<='6'):
                curr=curr+pre
            pre=tmp
        return curr

    def numDecodingV2(self,s):
        if s[0]=='0':
            return 0
        #动态规划
        dp=[0 for _ in range(len(s))] #表示截至下标i的数量
        dp[0]=1
        for i in range(1,len(s)):
            if s[i]=='0' and (s[i-1]>'2' or s[i-1]=='0'):
                return 0
            # 后两位为10或者20
            if s[i]=='0' and (s[i-1]=='1' or s[i-1]=='2'):
                if i>1:
                    dp[i]=dp[i-2]
                else:
                    dp[i]=1
            #后两位为21-26 或者11-19
            elif s[i-1]=='1' or (s[i-1]=='2' and s[i]>='1' and s[i]<='6'):
                if i>1:
                    dp[i]=dp[i-1]+dp[i-2]
                else:
                    dp[i]=dp[i-1]+1
            else:
                dp[i]=dp[i-1]
        return dp[-1]

if __name__ == "__main__":
    s=Solution()
    print(s.numDecoding('1'))
    pass 