#include <iostream>

using namespace std;

class Node{
    public:
        int data;
        Node* right;
        Node*left;

        Node(int value): data(value) {
            right = nullptr;
            left = nullptr;
        }
};
class Tree{
    public:
        Node* root = nullptr;
        
        Tree(){ root = nullptr; }
        Node* insert(Node* head, int value){
            if( head == nullptr ) {
                head =  new Node(value);
                if( root == nullptr){
                    root = head;
                }
                return head;
            }
            if( head->data > value){
                head->left = insert(head->left, value);
            }else{
                head->right =  insert(head->right, value);
            }
            return head;
        }

        void insert(int value){
            insert(root, value);
        }

        void preOrderTraversal(Node* head){
            if( head == nullptr ) return;
            cout << head->data << " ";
            preOrderTraversal(head->left);
            preOrderTraversal(head->right);
        }
        
        void inOrderTraversal(Node* head){
            if( head == nullptr ) return;
            preOrderTraversal(head->left);
            cout << head->data << " ";
            preOrderTraversal(head->right);
        }

        void leafOrderTraversal(Node* head){
            if( head == nullptr ) return;
            leafOrderTraversal(head->left);
            if( head-> left == nullptr && head-> right == nullptr)
                cout << head->data << " ";
            leafOrderTraversal(head->right);
        }

        void preOrderTraversal(){
            preOrderTraversal(root);
            cout << endl;
        }
        void leafOrderTraversal(){
            leafOrderTraversal(root);
            cout << endl;
        }
};

int main(){

    Tree* myList = new Tree();
    int number;
    while( cin >> number){
        if( number == -1)
            break;
        myList->insert(number);
    }

    cout << "preOrderTraversal" << endl;
    myList->preOrderTraversal();
    cout << "leafOrderTraversal" << endl;
    myList->leafOrderTraversal();
    // cout << "postOrderTraversal" << endl;
    // myList->postOrderTraversal();
    // cout << "rightOrderTraversal" << endl;
    // myList->rightOrderTraversal();

    return 0;
}