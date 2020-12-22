#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/16
# Solution:
import math

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # 以下代码出错，当链表位数足够长时，根本无法用int表示
    def addTwoNum(self,l1,l2):
        n1 = l1.val
        i = 1
        while l1.next:
            l1=l1.next
            n1 = n1+l1.val*math.pow(10,i)
            i += 1
        n2 = l2.val
        j = 1
        while l2.next:
            l2 = l2.next
            n2 = n2+l2.val*math.pow(10, j)
            j += 1
        n3=int(n1+n2)
        k=1
        result=[]
        if n3<10:
            return ListNode(n3)
        while n3>=10:
            var=int(n3-int(n3/math.pow(10,k))*math.pow(10,k))
            n3=n3-var
            result.append(int(var/math.pow(10,k-1)))
            k+=1
        head = ListNode(result[0])
        resultNode = head
        for i in range(1,len(result)):
            nodeB=ListNode(result[i])
            head.next=nodeB
            head=head.next

        return resultNode

    def addTwoNumV2(self,l1,l2):
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y
            carry = int(sum / 10)
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if l1!=None:
                l1 = l1.next
            if l2!=None:
                l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next

if __name__=="__main__":
    a=ListNode(2)
    b=ListNode(8)
    s=Solution()
    print(s.addTwoNumV2(a,b))

