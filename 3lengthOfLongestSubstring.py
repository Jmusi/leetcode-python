#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/12/27
# Solution:
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''

def lengthOfLongestSubstring(s):
    occ=set()
    n=len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动

    rk,ans=-1,0

    for i in range(n):
        if i!=0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[i-1])
        while rk+1<n and s[rk+1] not in occ:
            occ.add(s[rk+1])
            # 不断地移动右指针
            rk+=1
        ans=max(ans,rk-i+1)
    return ans
if __name__ == "__main__":
    print(lengthOfLongestSubstring('abcabcbb'))
    pass 