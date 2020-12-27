#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/12/27
# Solution:
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def addTwoNumbers(l1,l2):
    dummy=ListNode(-1)
    curr=dummy
    carry=0
    while l1!=None or l2!=None:
        l1_val=l1.val if l1 else 0
        l2_val=l2.val if l2 else 0
        val=(l1_val+l2_val+carry)%10
        carry=(l1_val+l2_val+carry)//10
        curr.next=ListNode(val)
        curr=curr.next
        if l1!=None:
            l1=l1.next
        if l2!=None:
            l2=l2.next
    if carry>0:
        curr.next=ListNode(carry)
    return dummy.next

if __name__ == "__main__":
    a=ListNode(2)
    b=ListNode(4)
    c=ListNode(3)
    a.next=b
    b.next=c

    d=ListNode(5)
    e=ListNode(6)
    f=ListNode(4)
    d.next=e
    e.next=f
    print(addTwoNumbers(a,d))
