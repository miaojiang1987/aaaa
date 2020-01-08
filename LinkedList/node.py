# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None



head=Node(5)
node1=Node(6)
head.next=node1
print(head.val)
print(head.next.val)        
        