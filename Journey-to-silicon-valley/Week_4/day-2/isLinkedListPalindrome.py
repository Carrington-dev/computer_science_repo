# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        stack = deque()

        while current != None:
            stack.append(current)
            current = current.next
        
        current = head
        while current != None:
            top = stack.pop()
            if current.val != top.val:
                return False
            current = current.next
        
        return True
        
