#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/6
# Solution: 移动窗口
class Solution:
    def minWindow(self,s,t):
        need={}
        window={}
        for c in t:
            need[c]=need.get(c,0)+1
        left,right=0,0
        result=None
        while right<len(s):
            c=s[right]
            right+=1
            #更新窗口内数据更新
            if need.get(c):
                window[c]=window.get(c,0)+1
                print('move right ',s[left:right])
                #判断左侧窗口是否要收缩
                while left<=right and self.check_valid(need,window):
                    if result == None or len(result) > right - left:
                        result = s[left:right]
                    print('move left ',s[left:right],result)
                    left_c=s[left]
                    left+=1
                    if need.get(left_c):
                        window[left_c]=window.get(left_c)-1
        return '' if result==None else result
    def check_valid(self,need,window):
        for c in need:
            if window.get(c,0)<need.get(c):
                return False
        return True
if __name__ == "__main__":
    s=Solution()
    print(s.minWindow('ADOBECODEBANC','ABC'))
    pass 