#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/17
# Solution:https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode/
# 回文可以从它的中心展开，并且只有 2n - 12n−1 个这样的中心

class Solution:
    def longestPalindrome(self,s):
        if s==None or len(s)<1:
            return ""
        start=0
        end=0
        for i in range(len(s)):
            lens1=self.expandAroundCenter(s,i,i)
            lens2=self.expandAroundCenter(s,i,i+1)
            result=max(lens1,lens2)

            if result>end-start:
                start=i-int((result-1)/2)
                end=i+int(result/2)
        return ''.join(s[start:end+1])

    def expandAroundCenter(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
if __name__ == "__main__":
    s=Solution()
    print(s.longestPalindrome('absbadf'))