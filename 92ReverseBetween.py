#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/17
# Solution:
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def reverseBetween(self,head,m,n):
        # 递归，参考字符串反转，一头一尾，交换位置
        if not head:
            return None
        left,right=head,head
        stop=False

        def recurseAndReverse(right,m,n):
            nonlocal left,stop
            if n==1:
                return
            right=right.next
            if m>1:
                left=left.next
            recurseAndReverse(right,m-1,n-1)
            if left==right or right.next==left:
                stop=True

            if not stop:
                left.val,right.val=right.val,left.val
                left=left.next
        recurseAndReverse(right,m,n)
        return head

    tmp = None  # 记录第n+1节点
    def reverseN(self,head,n):
        if n==1:
            self.tmp=head.next #记录n+1的节点
            return head
        last=self.reverseN(head.next, n-1)
        head.next.next=head
        head.next=self.tmp

        return last

    def reverseBetweenV2(self,head,m,n):
        if m==1:
            return self.reverseN(head,n)
        last=self.reverseBetweenV2(head.next,m-1,n-1)
        head.next=last
        return head
    def reverseBetweenV3(self,head,m,n):
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for _ in range(m-1):
            p = p.next
        cur = p.next
        for _ in range(n-m):
            q = cur.next
            cur.next = q.next # remove q from linked list
            q.next = p.next
            p.next = q

        return dummy.next
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
    c=s.reverseBetweenV2(n1,2,4)
    pass 