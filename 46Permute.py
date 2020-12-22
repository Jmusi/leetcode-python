#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/27
# Solution:
class Solution:
    def permute(self,nums):
        result=[]
        #track表示当前已存在的元素，可选择的元素为：nums中但不存在track中的元素
        def backtrack(nums,track):
            if len(track)==len(nums):
                result.append(track[:]) #此处必须为track[:]表示拷贝值
                return
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums,track)
                track.pop()

        backtrack(nums,[])
        return result
if __name__ == "__main__":
    s=Solution()
    print(s.permute([1,2,3]))
    pass 