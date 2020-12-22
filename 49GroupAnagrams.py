#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/28
# Solution:
class Solution:
    def groupAnagrams(self,strs):
        dic={}
        for s in strs:
            key_v=tuple(sorted(s))
            tmp=dic.get(key_v,[])
            tmp.append(s)
            dic[key_v]=tmp
        return list(dic.values())
if __name__ == "__main__":
    s=Solution()
    print(s.groupAnagrams(['eat','tea','tan','ate','nat','bat']))
    pass 