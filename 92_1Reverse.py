#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/17
# Solution:
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    #反转整个链表
    def reverse(self,head):
        if head.next == None:
            return head
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last
    #反转链表前N个数
    tmp = None  # 记录第n+1节点
    def reverseN(self,head,n):
        if n==1:
            self.tmp=head.next #记录n+1的节点
            return head
        last=self.reverseN(head.next, n-1)
        head.next.next=head
        head.next=self.tmp

        return last

if __name__ == "__main__":
    n1=ListNode(1)
    n2=ListNode(2)
    n3=ListNode(3)
    n4=ListNode(4)
    n5=ListNode(5)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5

    s=Solution()
    #b=s.reverse(n1)
    c=s.reverseN(n1,3)
    pass 