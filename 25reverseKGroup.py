#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/22
# Solution:

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution:
    def reverse(self,head,tail):
        prev=tail.next
        p=head
        while prev!=tail:
            nex=p.next
            p.next=prev
            prev=p
            p=nex
        return tail,head
    def reverseKGroup(self,head,k):
        hair=ListNode(0)
        hair.next=head
        pre=hair

        while head:
            tail=pre
            for i in range(k):
                tail=tail.next
                if not tail:
                    return hair.next
            nex=tail.next
            head,tail=self.reverse(head,tail)
            pre.next=head
            tail.next=nex
            pre=tail
            head=tail.next

        return hair.next
if __name__ == "__main__":
    a=ListNode('1')
    b=ListNode('3')
    c=ListNode('5')
    d=ListNode('2')
    e=ListNode('4')
    f=ListNode('6')
    a.next=b
    b.next=c
    c.next=d
    d.next=e
    e.next=f
    s=Solution()
    tmp=s.reverseKGroup(a,3)
    #c.next=cc

    pass 