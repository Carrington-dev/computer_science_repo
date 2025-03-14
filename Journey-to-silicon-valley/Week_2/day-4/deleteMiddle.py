# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        if head.next == None:
            return
        count = 0
        current = head
        context = []
        while current != None:
            context.append(current)
            current = current.next
            count += 1
        
        # print([ i.val for i in context].pop(count // 2))
        try:
            context[count // 2 - 1].next = context[count // 2 - 1].next.next
        except:
            pass
        return head
        
        