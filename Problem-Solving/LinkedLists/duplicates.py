# Definition for singly-linked list.
from typing import Optional

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

    
    def print(self, head):
        if head == None:
            return 
        print(head.val, sep=" ", end=" ")
        self.print(head.next)
    
    def removeDuplicates(self, head, prev =None):
        if head == None:
            return head
        if prev != None and head.val == prev.val:
            curr = head
            while curr.val == prev.val and (curr != None or prev != None):
                curr = curr.next
                if curr == None:
                    break
            prev.next = curr
        #print(head, head.next)
        self.removeDuplicates(head.next, head)

    def removeDuplicatesOther(self, head, next = None):
        if head == None:
            return head
        if next == None:
            return head
        if head.val == next.val:
            head.next = next.next
        self.removeDuplicatesOther(next, next.next)    

# 1 1 2 3 3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f"{ self.val }"

"""

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if( head == None ):
#             return
#         if head.next.data == head.data:
#             head.next = head.next.data
#         self.deleteDuplicates(head->next)

"""    

listt = LinkedList()
x = int(input())
while x != -1:
    listt.insert(listt.head, x)
    x = int(input())

listt.print(listt.head)
listt.removeDuplicates(listt.head)
# listt.removeDuplicatesOther(listt.head, listt.head.next)
print()
listt.print(listt.head)