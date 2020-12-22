#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/23
# Solution: # 有一种O(n)的移动窗口法，见下：
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-6/
class Solution:
    def findSubString(self,s,words):
        #O(n*m)
        if words==None or s==None or len(s)<=0 or len(words)<=0:
            return []
        word_dict={}
        word_lens=len(words[0])
        s_lens=len(s)
        result=[]
        for w in words:
            word_dict[w]=word_dict.get(w,0)+1
        for i in range(0,s_lens-word_lens*len(words)+1):
            tmp=s[i:i+word_lens*len(words)]
            cur_word_dict={}
            #检查截取的字符串是否满足要求
            for j in range(0,len(tmp),word_lens):
                word=tmp[j:j+word_lens]
                if not word_dict.get(word):
                    break
                if cur_word_dict.get(word,0)>word_dict.get(word):
                    break
                cur_word_dict[word]=cur_word_dict.get(word,0)+1

                if cur_word_dict == word_dict:
                    result.append(i)
        return result

if __name__ == "__main__":
    s=Solution()
    print(s.findSubString('barfoothefoobar',['bar','foo']))
    pass 