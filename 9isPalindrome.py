#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/12/27
# Solution:

def isPalindrome(x):
    str_x=str(x)
    left,right=0,len(str_x)-1
    while left<right:
        if str_x[left]!=str_x[right]:
            return False
        left+=1
        right-=1
    return True
def isPalindromev2(x):
    #注意此处x%10的判断
    if x<0 or (x!=0 and x%10==0):
        return False
    right_rev=0
    while x>right_rev:
        right_rev=right_rev*10+x%10
        x=x//10
    return x==right_rev or x==right_rev//10
if __name__ == "__main__":
    print(isPalindromev2(1221))
    pass 