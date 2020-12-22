#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/11
# Solution:
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def deleteDuplicates(self,head):
        if head==None or head.next==None:
            return head
        dumpy=ListNode(0)
        result=dumpy
        while head!=None and head.next!=None:
            if head.val!=head.next.val:
                dumpy.next=ListNode(head.val)
                dumpy=dumpy.next
                head=head.next
            else:
                tmp=head.val
                while head!=None and head.val==tmp:
                    head=head.next
        if head!=None:
            dumpy.next=ListNode(head.val)
        return result.next

    def deleteDuplicatesV2(self,head):
        if not head or not head.next:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        a=dummy
        b=head
        while b and b.next:
            if a.next.val!=b.next.val:
                a=a.next
                b=b.next
            else:
                while b and b.next and a.next.val==b.next.val:
                    b=b.next
                a.next=b.next
                b=b.next
        return dummy.next
if __name__ == "__main__":
    n1=ListNode(1)
    n2=ListNode(1)
    n3=ListNode(2)
    n4=ListNode(3)
    n5=ListNode(3)
    n6=ListNode(4)
    n7=ListNode(4)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    n5.next=n6
    n6.next=n7
    s=Solution()
    print(s.deleteDuplicates(n1))
    pass 