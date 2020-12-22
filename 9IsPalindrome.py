#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/19
# Solution:

class Solution:
    def isPalindrome(self,num):
        a=str(num)
        b=a[::-1]
        return a==b

    def isPalindromeV2(self,x):
        if x<0 or (x!=0 and x%10==0):
            return False
        right_rev = 0
        while x > right_rev:
            right_rev = right_rev*10 + x%10
            x = x//10
        return x==right_rev or x==right_rev//10
if __name__ == "__main__":
    s=Solution()
    print(s.isPalindrome(-12321))
    pass 