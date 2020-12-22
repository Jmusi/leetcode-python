#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/22
# Solution:

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution:
    def swapPairs(self,head):
        if not head or head.next==None:
            return head
        first_node=head
        second_node=head.next

        first_node.next=self.swapPairs(second_node.next)
        second_node.next=first_node

        return second_node

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
    tmp=s.swapPairs(a)
    pass 