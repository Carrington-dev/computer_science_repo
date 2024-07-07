def mergeLists(head1, head2):
    result = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
        
    if head1.data <= head2.data:
        result = head1
        result.next = mergeLists(head1.next, head2)
    else:
        result = head2
        result.next = mergeLists(head2.next, head1)
    
    return result