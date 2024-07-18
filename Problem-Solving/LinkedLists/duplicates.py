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
        # if head.next and head.val == head.next.val:
        #     head.next = head.next.next
        # self.removeDuplicates(head.next)
        if prev != None and head.val == prev.val:
            curr = head
            while curr.val == prev.val and curr != None and prev != None:
                curr = curr.next
            prev.next = curr
        self.removeDuplicates(head.next, head)
        


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

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
print()
listt.print(listt.head)