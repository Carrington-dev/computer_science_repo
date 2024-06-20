#include <iostream>

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

            if( head -> data < value){
                head -> left = insert( head-> left, value);
            }else{
                head -> right = insert( head-> right, value);
            }
            return head;
        }

        void insert(int value){
            insert(root, value);
        }


        void preOrderTraversal(Node* root){
            if(root == nullptr) return;
            cout << root -> data << " ";
            preOrderTraversal(root ->left);
            preOrderTraversal(root ->right);
        }
        void preOrderTraversal(){
            preOrderTraversal(root);
            cout << endl;
        }
        void inOrderTraversal(Node* root){
            if(root == nullptr) return;
            inOrderTraversal(root ->left);
            cout << root -> data << " ";
            inOrderTraversal(root ->right);
        }
        void inOrderTraversal(){
            inOrderTraversal(root);
            cout << endl;
        }

        void postOrderTraversal(Node* root){
            if(root == nullptr) return;
            postOrderTraversal(root ->left);
            postOrderTraversal(root ->right);
            cout << root -> data << " ";
        }
        void postOrderTraversal(){
            postOrderTraversal(root);
            cout << endl;
        }
};

int main(){
    Tree* myList = new Tree();
    int number;
    while( cin >> number){
        myList->insert(number);
    }
    return 0;
}