#include <iostream>
#include <queue>

using namespace std;

class Node{
    public:
        int data;
        Node* left;
        Node* right;
        Node(int value): data(value) { right = nullptr; left = nullptr; }
};

class Tree{
    public:
        Node* root;
        Tree(){
            root = nullptr;
        }

        Node* insert( Node* head, int value ){
            if( head == nullptr ){
                head = new Node(value);
                if( root == nullptr){
                    root = head;
                    return root;
                }
                return head;
            }

            if( head -> data > value){
                head -> left = insert( head-> left, value);
            }else{
                head -> right = insert( head-> right, value);
            }
            return head;
        }

        void insert(int value){
            insert(root, value);
        }
};


int main(){
    
    return 0;
}