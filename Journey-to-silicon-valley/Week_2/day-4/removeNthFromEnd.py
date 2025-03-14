
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return
        if head.next == None:
            return
        
        length = 0
        current = head
        context = []
        while current != None:
            context.append(current)
            current = current.next
            length += 1
        
        # print([ i.val for i in context].pop(count // 2))
        endPoint = length - n - 1
        context[endPoint].next = context[endPoint].next.next
        return head
        
        