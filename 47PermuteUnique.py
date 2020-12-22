#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/28
# Solution: 和46题的区别在于，本题的nums可能会出现重复数字，要求排列不可重复
class Solution:
    def permuteUnique(self,nums):
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        result=[]
        def backtrack(dic,track):
            if len(track)==len(nums):
                result.append(track[:])
                return
            for i in dic.keys():
                #在会产生重复结果集的地方剪枝
                if dic[i]==0:
                    continue
                dic[i]-=1
                track.append(i)
                backtrack(dic,track)
                track.pop()
                dic[i]+=1
        backtrack(dic,[])
        return result

    def permuteUniqueV2(self,nums):
        #排序后和前一个元素值相同（此处隐含这个元素的index>0），并且前一个元素还没有被使用过

        nums.sort()
        res=[]
        check=[0 for _ in range(len(nums))] #表示该元素是否被用过
        def backtrack(track,nums,check):
            if len(track)==len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if check[i]==1:
                    continue
                #为什么要添加check[i-1]==0,可以参考视频https://leetcode-cn.com/problems/permutations-ii/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liwe-2/
                #check[i-1]=0表示上一个相同元素被撤销了选择，即对应的排列已经完全填充了
                if i>0 and nums[i]==nums[i-1] and check[i-1]==0:
                    continue
                check[i]=1
                track.append(nums[i])
                backtrack(track,nums,check)
                track.pop()
                check[i]=0

        backtrack([],nums,check)
        return res
if __name__ == "__main__":
    s=Solution()
    print(s.permuteUniqueV2([1,1,1,2]))
    pass 