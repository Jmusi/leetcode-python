#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/24
# Solution: 回溯
# 根据示例 1：输入: candidates = [2,3,6,7]，target = 7。
# 候选数组里有 2 ，如果找到了 7 - 2 = 5 的所有组合，再在之前加上 2 ，就是 7 的所有组合；
# 同理考虑 3，如果找到了 7 - 3 = 4 的所有组合，再在之前加上 3 ，就是 7 的所有组合，依次这样找下去
class Solution:
    def combinationSum(self, candidates, target):
        size=len(candidates)
        if size==0:
            return []
        candidates.sort()
        path=[]
        res=[]
        self.dfs(candidates,0,size,path,res,target)
        return res

    def dfs(self,candiates,begin,size,path,res,target):
        #递归终止条件
        if target==0:
            res.append(path[:])
            return
        for index in range(begin,size):
            residue=target-candiates[index]
            if residue<0:
                break # 剪枝，后续参数不需要尝试
            path.append(candiates[index])
            # 下一层从index开始，表示可以重复使用
            self.dfs(candiates,index,size,path,res,residue)
            path.pop()
if __name__ == "__main__":
    s=Solution()
    print(s.combinationSum([2,3,6,7],7))
    pass 