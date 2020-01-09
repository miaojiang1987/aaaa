# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    

def print_list(head):
    cur=head
    result=""
    while cur:
        result+=str(cur.val)+"->"
        cur=cur.next
    result+="None"
    print(result)
    return result
        
'''
head=Node(-1)
cur=head
for i in range(5):
    cur.next=Node(i)
    cur=cur.next

print_list(head)
'''
#head=Node(5)
#node1=Node(6)
#head.next=node1
#print(head.val)
#print(head.next.val)        
        