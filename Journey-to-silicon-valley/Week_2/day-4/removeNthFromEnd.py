
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        current = head
        context = []
        while current != None:
            context.append(current)
            current = current.next
            length += 1
        
        endPoint = length - n - 1
        if endPoint == -1:
            return head.next
        context[endPoint].next = context[endPoint].next.next
        return head
        
        