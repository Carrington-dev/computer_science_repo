#include <iostream>

using namespace std;

class Node{
    public:
        int data;
        Node* left;
        Node* right;

        Node(int x): data(x) {
            left = nullptr;
            right = nullptr;
        }
};

class Tree{
    public:
        Node* root;
        Tree(){ root = nullptr; }

        Node* insert(Node* &head, int data){
            if(head == nullptr) {
                if( root == nullptr){
                    head = new Node(data);
                    return head;
                }
                return new Node(data);
            }

            if( head->data > data ){
                head->left = insert(head->left, data);
            }else{
                head->right = insert(head->right, data);
            }
            return head;
        }

        void print(Node* head){
            if(head == nullptr) return;
            cout << head->data << " ";
            print(head->left);
            print(head->right);
        }

        void print(){
            cout << "Printing With Pre-Order Traversal" << endl;
            print(root);
            cout << endl;
        }

        void insert(int data){
            insert(root, data);
            // cout << endl;
        }

        void printLeft(Node* head){
            if(head == nullptr) return;
            cout << head->data << " ";
            print(head->left);
            // print(head->right);
        }

         void printLeft(){
            cout << "Printing With Pre-Order Traversal left Nodes only" << endl;
            printLeft(root);
            cout << endl;
        }
};

int main(){
    Tree* a = new Tree();
    int c;
    cin >> c;
    while( c != -1)
    {
        a->insert(c);
        cin >> c;
    }
    // 50, 70, 60, 20, 90, 10, 40, 100 -1
    // 25 20 36 10 22 30 40 5 12 28 38 48 -1


    a->print();
    a->printLeft();
    return 0;
}