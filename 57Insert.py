#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/31
# Solution:
class Solution:
    def insert(self,intervals,newInterval):
        new_start,new_end=newInterval
        idx,n=0,len(intervals)
        output=[]
        # 所有起始点小于new_start的值直接添加到result
        while idx<n and new_start>intervals[idx][0]:
            output.append(intervals[idx])
            idx+=1
        # 插入新值，并更新边界
        if not output or output[-1][1]<new_start:
            output.append(newInterval)
        else:
            output[-1][1]=max(output[-1][1],new_end)

        while idx<n:
            interval=intervals[idx]
            start,end=interval
            idx+=1
            if output[-1][1]<start:
                output.append(interval)
            else:
                output[-1][1]=max(output[-1][1],end)
        return output
if __name__ == "__main__":
    s=Solution()
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
    pass 