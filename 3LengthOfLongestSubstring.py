#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/17
# Solution: 从每一个字符开始的，不包含重复字符的最长子串，那么其中最长的那个字符串即为答案

class Solution:
    def lengthOfLongestSubstring(self, s):
        occ=set()
        n=len(s)
        rk,ans=-1,0

        for i in range(n):
            if i!=0:
                occ.remove(s[i-1])
            while rk+1<n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk+=1
            ans=max(ans,rk-i+1)
        return ans

if __name__=='__main__':
    string='pawwswk'
    s=Solution()
    print(s.lengthOfLongestSubstring(string))