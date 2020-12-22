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
        current=head
        while current!=None and current.next!=None:
            if current.next.val==current.val:
                current.next= current.next.next
            else:
                current=current.next
        return head




if __name__ == "__main__":
    pass 