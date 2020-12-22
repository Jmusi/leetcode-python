#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/22
# Solution:
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def mergeKLists(self,lists):

        def merge2Lists(l1,l2):
            if l1==None:
                return l2
            if l2==None:
                return l1
            if l1.val<l2.val:
                l1.next=merge2Lists(l1.next,l2)
                return l1
            else:
                l2.next=merge2Lists(l1,l2.next)
                return l2

        def merge(lists,left,right):
            if left==right:
                return lists[left]
            if left>right:
                return None
            mid=(left+right)//2
            return merge2Lists(merge(lists,left,mid),merge(lists,mid+1,right))

        return merge(lists, 0, len(lists)-1)


if __name__ == "__main__":
    a=ListNode('1')
    b=ListNode('3')
    c=ListNode('5')
    #cc=ListNode('5')
    a.next=b
    b.next=c
    #c.next=cc
    d=ListNode('2')
    e=ListNode('4')
    f=ListNode('6')
    d.next=e
    e.next=f
    s=Solution()
    tmp=s.mergeKLists([a,d])
    pass 