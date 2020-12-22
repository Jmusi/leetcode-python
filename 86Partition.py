#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/14
# Solution:
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def partition(self,head,x):
        before =before_head= ListNode(0)
        after = after_head=ListNode(0)

        while head:
            if head.val<x:
                before.next=head
                before=before.next
            else:
                after.next=head
                after=after.next
            head=head.next
        after.next=None
        before.next=after_head.next
        return before_head.next
if __name__ == "__main__":
    pass 