#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/21
# Solution:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self,head,n):
        # 两遍扫描法
        dumpy=ListNode(0) #初始化一个哑头节点，方便处理
        dumpy.next=head
        tmp=head
        lens=1
        while tmp.next!=None:
            lens+=1
            tmp=tmp.next
        pos=lens-n #这个位置的节点next要指向下下一个节点
        first=dumpy
        while pos>0:
            pos-=1
            first=first.next
        first.next= first.next.next
        return dumpy.next
    # 两个指针，中间间隔n，当第二个指针到达末尾，则第一个指针到达需要移除的位置
    def removeNthFromEndV2(self,head,n):
        dumpy=ListNode(0)
        dumpy.next=head
        first=dumpy #此处要初始化为dumpy，不能为head，否则会导致原始只有一个节点，移除后为空的问题
        second=dumpy
        while n>0:
            second=second.next
            n-=1

        while second.next!=None:
            first=first.next
            second=second.next
        first.next=first.next.next
        return dumpy.next
if __name__ == "__main__":
    a=ListNode(1)
    b=ListNode(2)
    c=ListNode(3)
    d=ListNode(4)
    e=ListNode(5)
    a.next=b
    b.next=c
    c.next=d
    d.next=e

    s=Solution()
    tmp=s.removeNthFromEndV2(e,1)
    print(tmp)
    pass 