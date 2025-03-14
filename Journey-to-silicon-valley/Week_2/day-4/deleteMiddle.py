from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        while current != None:
            current = current.next
            count += 1
        
        middle = count // 2
        new_current = head
        new_prev = None
        new_count = 0
        while current != None:
            next = new_current.next
            new_prev = current
            current = next
            count += 1
            if new_count == count:
                break
        new_prev.next = current.next
        