#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/18
# Solution: 回溯，3个点.所有可能放置的位置
class Solution:
    def restoreIpAddresses(self,s):
        def valid(segment):
            return int(segment)<=255 if segment[0]!='0' else len(segment)==1
        def update_output(curr_pos):
            segment=s[curr_pos+1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1,dots=3):
            for curr_pos in range(prev_pos+1,min(n-1,prev_pos+4)):
                segment=s[prev_pos+1:curr_pos+1]
                if valid(segment):
                    segments.append(segment)
                    if dots-1==0:
                        update_output(curr_pos)
                    else:
                        backtrack(curr_pos,dots-1)
                    segments.pop()
        n=len(s)
        output,segments=[],[]

        backtrack()
        return output
if __name__ == "__main__":
    s=Solution()
    print(s.restoreIpAddresses('000256'))
    pass 