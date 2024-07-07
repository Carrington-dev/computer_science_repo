#include <iostream>

using namespace std;

class Node{
    public:
        int data;
        Node* next;
        Node(int number): data(number){ next = nullptr; };

};

class LinkedList{

    public:
        Node* header = nullptr;
        LinkedList(){ header = nullptr; }
       
        Node* insert(Node* head, int data){
            // cout << "I ran insert -> head, data " << endl;
            if( head == nullptr){
                head = new Node(data);
                // cout << "I ran insert -> head == nullptr " << head -> data << endl;
                if ( header == nullptr)
                {
                    header = head;
                } 
                return head;
            }
            // cout << "I ran insert -> head != nullptr " << endl;
            head->next =  insert( head -> next, data);
            return head;
        }

        void insert(int data){
            insert(header, data);
        }

        void print(Node* root ){
            if( root == nullptr)
                return;
            cout << root->data << " " ;
            print(root -> next);
        }

        void print(){
            print(header);
        }

        int length(){
            return  getLength(header);
        }

        int getLength(Node* root, int length = 0){
            if( root == nullptr){
                return length;
            }
            return getLength(root -> next, length + 1);
        }
        /* Using recursion to reverse a linkedList */
        Node* reverse(Node* head){
            if( head == nullptr){
                return nullptr;
            }

            Node* current = head;
            Node* previous = nullptr;

            while( current != nullptr ){
                Node* next = current->next;
                current->next = previous;
                previous = current;
                current = next;
            }
            header = previous;
            return header;
        }


        /* Using iteration or while loop to reverse a linked list */
        void reverse(){
            reverse(header);
        }
        /* Using while loops to merge lists (linked lists) */
        
};

Node* merge(Node* head_one, Node* head_two){
    if( head_one == nullptr ) return head_two;
    if( head_two == nullptr ) return head_one;
    Node* result;
    if( head_one -> data < head_two ->data)
        {
            result = head_one;
            result->next = merge(result, head_two);
        }
    else{
        result = head_two;
        result->next = merge(head_one, result);
    }

    return result;
}


/*
Node* merge(LinkedList* list_one, LinkedList* list_two){
    if(list_one->header == nullptr && list_two == nullptr){
        return nullptr;
    }
    if( list_one->header ==  nullptr) return list_two->header;
    if( list_two->header ==  nullptr) return list_one->header;

    Node* tail = nullptr;
    Node* current_one = list_one->header;
    Node* current_two = list_two->header;

    

    while( current_one != nullptr && current_two != nullptr){
        if( current_one -> data < current_two -> data){
            Node* next = current_one -> next;
            tail = current_one;
        }else{
            tail = current_two;
        }
    }
}
*/

/*
1 3 5 7 9 11
2 4 8 10 12 14

1 -> 2 -> 3 -> 4 -> 5 -> 
*/

int main(){
    LinkedList* list_one = new LinkedList();
    LinkedList* list_two = new LinkedList();
    LinkedList* list_three = new LinkedList();
    for (int i = 0; i <= 20; i+=2)
    {
        list_one->insert(i);
    }
    for (int i = 1; i <= 20; i+=2)
    {
        list_two->insert(i);
    }
    
    list_one->print();
    cout << endl;
    // list_one->reverse();
    list_two->print();
    cout << endl;
    Node* node = merge(list_one->header, list_two->header);
    list_three->header = node;
    // list_three->print(node);
    cout << node->data << endl;
    cout << endl;
    cout << "The length of a tree is " << list_one->length() << endl;
    return 0;
}
