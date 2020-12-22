#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/2
# Solution:
class Solution:
    def simplifyPath(self,path):
        r = []
        for s in path.split('/'):
            r = {'': r, '.': r, '..': r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)

if __name__ == "__main__":
    s=Solution()
    print(s.simplifyPath('/../'))
    pass 