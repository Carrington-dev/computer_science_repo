# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f"{ self.val }"


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, head,  x):
        if( head is None ):
            head  = ListNode(x)
            if self.head is None:
                self.head = head
            return head
        head.next = self.insert(head.next, x)
        return head
    
    def hasACycle(self, head):
        context =  {}
        return self.hasACycleTester(head, context)

    def hasACycleTester(self, head, allNodes):
        if head == None:
            return False
        elif head not in allNodes:
            allNodes[head] = head
        elif head in allNodes:
            return True
        return self.hasACycleTester(head.next, allNodes)

