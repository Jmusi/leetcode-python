#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/24
# Solution:
from collections import OrderedDict
class Solution:
    def countAndSay(self,n):
        tmp='1'
        for i in range(n-1):
            newTmp=''
            last_char_count=None
            last_char=None
            for j in range(len(tmp)):
                if j==0:
                    last_char=tmp[j]
                    last_char_count=1
                elif tmp[j]==tmp[j-1]:
                    last_char_count+=1
                else:
                    newTmp += str(last_char_count) + last_char
                    last_char=tmp[j]
                    last_char_count=1
            newTmp += str(last_char_count) + last_char

            tmp=newTmp
        return tmp
if __name__ == "__main__":
    s=Solution()
    print(s.countAndSay(6))
    pass 