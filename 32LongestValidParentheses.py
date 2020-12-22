#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/23
# Solution: 准确的应该使用动态规划
class Solution:
    def longestValidParentheses(self,s):
        # O(n^2)
        if s==None or len(s)<2:
            return 0
        cur_max=0
        for i in range(len(s)):
            if s[i]==')':
                continue
            for j in range(i+1,len(s),2):
                if self.isValid(s[i:j+1]):
                    cur_max=max(cur_max,j-i+1)
        return cur_max
    def isValid(self,s):
        if s.startswith(')') or len(s)%2==1:
            return False
        chars=[]
        for c in s:
            if c==')':
                top_elem=chars.pop() if chars else "#"
                if not top_elem=='(':
                    return False
            else:
                chars.append(c)
        return not chars

    def longestValidParenthesesV2(self,s):
        # O(n),动态规划法
        if s==None or len(s)<2:
            return 0
        cur_max=0
        dp=[0]*len(s)
        dp[0]=0
        dp[1]=0
        for i in range(1,len(s)):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                    dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
                cur_max=max(cur_max,dp[i])
        return cur_max

    def longestValidParenthesesV3(self,s):
        # 1、栈底永远保存着当前有效子串的前一个字符的下标，就像个守门员一样守在那里，所以一开始要将-1放入栈中。
        # 2、遇到左括号就入栈；
        # 3、遇到右括号就将栈顶元素出栈。此时有两种情况：
        #（1）如果栈顶元素出栈后，栈内剩下的元素不为空，则说明弹出的这个栈顶元素一定是左括号，讲真，因为栈底有保险。
        #（2）如果栈顶元素出栈后，栈内为空，则说明刚刚弹出的这个栈顶元素就是之前的“有效子串前一位的字符下标”，守门员都没了，所以此时应该使用当前的右括号的下标入栈，更新这个“有效子串前一位的字符下标”。
        chars=[]
        cur_max=0
        chars.append(-1)
        for i in range(len(s)):
            if s[i]=='(':
                chars.append(i)
            else:
                chars.pop()
                if len(chars)==0:
                    chars.append(i)
                else:
                    cur_max=max(cur_max,i-chars[-1])

        return cur_max
if __name__ == "__main__":

    s=Solution()
    print(s.longestValidParenthesesV3('()'))
    pass 