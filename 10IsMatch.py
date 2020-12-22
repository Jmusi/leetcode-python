#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/19
# Solution: 实现.和*匹配的建议正则表达式功能 ？？？？
class Solution:
    def isMatch(self,s,p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'} # s不为空，且p[0]==s[0]或者p[0]=='.'

        if len(p)>=2 and p[1]=='*':
            return self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:],p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])
        return first_match

    def isMatchV2(self,s,p):
        if not p: return not s
        if not s and len(p) == 1: return False

        nrow = len(s) + 1
        ncol = len(p) + 1

        dp = [[False for c in range(ncol)] for r in range(nrow)]

        dp[0][0] = True
        dp[0][1] = False
        for c in range(2, ncol):
            j = c - 1
            if p[j] == '*': dp[0][c] = dp[0][c - 2]

        for r in range(1, nrow):
            i = r - 1
            for c in range(1, ncol):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False

        return dp[nrow - 1][ncol - 1]

if __name__ == "__main__":
    s=Solution()
    print(s.isMatch('abb','ab*'))
    pass 