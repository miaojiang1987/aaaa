# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:31:55 2020

@author: m_jia
"""

from node import Node
from node import print_list

# This problem 
def remove_duplicate(head):
    hashset=set()
    prev=None
    cur=head
    while cur!=None:
        value=cur.val
        if value in hashset:
            prev.next=cur.next
        

node1=Node(5)
print_list(node1)