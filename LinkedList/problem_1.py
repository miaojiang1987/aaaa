# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:31:55 2020

@author: m_jia
"""

from node import Node
from node import print_list

# This problem is to remove duplicate element from a list
# First solution allow to have a buffer 
def remove_duplicate(head):
    hashset=set()
    prev=None
    cur=head
    while cur!=None:
        value=cur.val
        if value in hashset:
            prev.next=cur.next
        else:
            hashset.add(value)
        prev=cur
        cur=cur.next
    return head

head=Node(3)
cur=head
cur.next=Node(4)
cur=cur.next
cur.next=Node(5)
cur=cur.next
cur.next=Node(5)
cur=cur.next
cur.next=Node(6)
cur=cur.next
print_list(head)
head=remove_duplicate(head)
print_list(head)