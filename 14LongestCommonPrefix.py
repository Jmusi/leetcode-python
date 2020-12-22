#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/20
# Solution:

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        prefix=strs[0] #初始化第一个字符串为公共前缀，然后依次减少长度
        # 依次将剩下的字符串对比找公共字符串
        for s in strs[1:]:
            while len(prefix)>0:
                if not s.startswith(prefix):
                    prefix=prefix[:-1]
                else:
                    break
        return prefix
if __name__ == "__main__":
    s=Solution()
    strs=["dog","racecar","car"]
    print(s.longestCommonPrefix(strs))
    pass 