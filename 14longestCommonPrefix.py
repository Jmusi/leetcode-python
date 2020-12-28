#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/12/28
# Solution:
def longestCommonPrefix(strs):
    if strs==[]:
        return ''
    prefix=strs[0]

    for s in strs[1:]:
        while prefix:
            if not s.startswith(prefix):
                prefix=prefix[:-1]
            else:
                break
    return prefix
if __name__ == "__main__":
    print(longestCommonPrefix(['flower','flow','flight']))
    pass 