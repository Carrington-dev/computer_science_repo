class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_node(self):
        pass

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

#time complixity = 0(N)
def mergeLists(head1, head2):
    temp_ptr1 = head1
    temp_ptr2 = head2
    new_list = SinglyLinkedList()
    while temp_ptr1 and temp_ptr2:
        #adding data first that is smaller than the other
        if temp_ptr1.data<=temp_ptr2.data:
            new_list.insert_node(temp_ptr1.data)
            temp_ptr1 = temp_ptr1.next
        else:
            new_list.insert_node(temp_ptr2.data)
            temp_ptr2 = temp_ptr2.next
         
    #inserting remaining data from either of list that is still having nodes data
    while temp_ptr1:
        new_list.insert_node(temp_ptr1.data)
        temp_ptr1 = temp_ptr1.next
    while temp_ptr2:
        new_list.insert_node(temp_ptr2.data)
        temp_ptr2 = temp_ptr2.next 
        
    return new_list.head