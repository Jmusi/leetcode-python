#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/24
# Solution: 和39的区别在于39可以无限次取原始，而本题限制组合中的每个数字在每个组合中只能使用一次 ，关键在于去除重复
class Solution:
    def combinationSum2(self,candidates,target):
        size=len(candidates)
        if size==0:
            return []
        candidates.sort()
        res=[]
        self.dfs(candidates,0,size,[],target,res)
        return res
    def dfs(self,candidates,begin,size,path,residue,res):
        if residue==0:
            res.append(path[:])
        for index in range(begin,size):
            if candidates[index]>residue:
                break
            # 跳过重复组合 （39题中index=begin表示本身可以无限重复）
            if index>begin and candidates[index-1]==candidates[index]:
                continue
            path.append(candidates[index])
            # 从index+1开始表示不能包含自身
            self.dfs(candidates,index+1,size,path,residue-candidates[index],res)
            path.pop()

if __name__ == "__main__":
    s=Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5],8))
    pass 