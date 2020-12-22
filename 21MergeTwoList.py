#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/22
# Solution:

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def mergeTwoList(self,l1,l2):
        if l1==None:
            return l2
        if l2==None:
            return l1
        newHead=ListNode(0)
        tmp=newHead
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                newHead.next=l1
                newHead=newHead.next
                l1=l1.next
            else:
                newHead.next=l2
                newHead=newHead.next
                l2=l2.next
        if l1==None:
            newHead.next=l2
        if l2==None:
            newHead.next=l1
        return tmp.next
    # 递归
    def mergeTwoListV2(self,l1,l2):
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<=l2.val:
            l1.next=self.mergeTwoListV2(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoListV2(l1,l2.next)
            return l2
if __name__ == "__main__":
    a=ListNode('1')
    b=ListNode('2')
    c=ListNode('4')
    #cc=ListNode('5')
    a.next=b
    b.next=c
    #c.next=cc
    d=ListNode('1')
    e=ListNode('3')
    f=ListNode('4')
    d.next=e
    e.next=f

    s=Solution()
    tmp=s.mergeTwoListV2(a,d)
    pass 