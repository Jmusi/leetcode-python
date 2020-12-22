#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/31
# Solution:
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def rotateRight(self,head,k):
        if head==None or head.next==None:
            return head

        dumpy=ListNode(0)
        dumpy.next=head
        total_node=1
        #先连成环，然后断开
        while head.next!=None:
            head=head.next
            total_node+=1
        head.next=dumpy.next

        i=0
        head=dumpy.next
        #取新的head节点的上一个节点，返回下一个节点之前把next=None
        for i in range(total_node-k%total_node-1):
            head=head.next
            i+=1
        result=head.next
        head.next=None
        return result

if __name__ == "__main__":
    a1=ListNode(1)
    a2=ListNode(2)
    a3=ListNode(3)
    a4=ListNode(4)
    a5=ListNode(5)
    # a1.next=a2
    # a2.next=a3
    # a3.next=a4
    # a4.next=a5

    s=Solution()
    print(s.rotateRight(a1,3))
    pass 