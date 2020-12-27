#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/12/27
# Solution:
'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
'''

def find_around_center(s,left,right):
    if s[left]!=s[right]:
        return ''
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    return s[left+1:right]

def longestPalindrome(s):
    # 以每个位置的中心向左右两端增加窗口
    cur_max=s[0]
    for i in range(len(s)-1):
        str1=find_around_center(s,i,i)
        str2=find_around_center(s,i,i+1)
        if len(str1)>len(str2):
            if len(str1)>len(cur_max):
                cur_max=str1
        else:
            if len(str2)>len(cur_max):
                cur_max=str2

    return cur_max


if __name__ == "__main__":
    print(longestPalindrome('aa'))
    pass 