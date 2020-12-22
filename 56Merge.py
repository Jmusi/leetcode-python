#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/31
# Solution:
class Solution:
    def merge(self,intervals):
        if len(intervals)<=1:
            return intervals
        result=[]
        intervals.sort(key=lambda x:x[0])
        start=intervals[0][0]
        end=intervals[0][1]
        for interval in intervals[1:]:
            cur_start=interval[0]
            cur_end=interval[1]
            if cur_start<=end:
                end=max(cur_end,end)
            else:
                result.append([start,end])
                start=cur_start
                end=max(cur_end,end)
        result.append([start,end])
        return result

if __name__ == "__main__":
    s=Solution()
    print(s.merge([[1,4],[2,3]]))
    pass 