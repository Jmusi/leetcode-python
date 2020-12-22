#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/23
# Solution: haystack 中查找needle的出现位置,
# 两个指针，分别指向两个字符串头，逐字符比较，一旦发现不匹配则返回之前位置的下一个位置

class Solution:
    def strStr(self,haystack,needle):
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
    def strStrV2(self,haystack,needle):
        if needle==None or needle=='':
            return 0
        cur_pos=0
        while cur_pos<len(haystack)-len(needle)+1:
            ph=cur_pos
            pn=0
            while haystack[ph]==needle[pn]:
                ph+=1
                pn+=1
                if pn==len(needle):
                    return cur_pos
            cur_pos+=1
        return -1


if __name__ == "__main__":
    s=Solution()
    print(s.strStrV2('helloll','ll'))
    pass 