#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/20
# Solution:

class Solution:
    romandict={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
    def roman2Int(self,s):
        i=0
        result=0
        while i<len(s):
            if self.romandict.get(s[i:i+2]):
                result+=self.romandict.get(s[i:i+2])
                i+=2
            elif self.romandict.get(s[i]):
                result+=self.romandict.get(s[i])
                i+=1
            else:
                raise IOError
        return result

if __name__ == "__main__":
    s=Solution()
    print(s.roman2Int('MMCMXCIX'))
    pass 