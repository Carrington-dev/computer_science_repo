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

        void printLeftNodes(){
            cout << "Printing With Left Leaves Only" << endl;
            printLeftNodes(root);
            traverseRightNodes(root->right);
            cout << endl;
        }

        void insert(int data){
            insert(root, data);
        }

        void printLeftNodes(Node* head){
            if(head == nullptr) return;
            cout << head->data << " ";
            printLeftNodes(head->left);
            
        }

        void traverseRightNodes(Node* head){
            if(head == nullptr) return;
            print(head->left);
            traverseRightNodes(head->right);
        }

        void printAllLeftNode(Node* head, bool isRightNode){
            if(head == nullptr) return;
            if(!isRightNode){
                cout << head->data << " ";
            }
            printAllLeftNode(head->left, false);
            printAllLeftNode(head->right, true);
        }

        void printAllLeftNode(){
            printAllLeftNode(root, false);
        }

};


int main(){
    Tree* tree = new Tree();
    int addedNumber;
    while( cin >> addedNumber)
    {
        if( addedNumber == -1){
            break;
        }
        tree->insert(addedNumber);
    }

    // 50, 70, 60, 20, 90, 10, 40, 100 -1
    // 25 20 36 10 22 30 40 5 12 28 38 48 -1
    // 25 20 36 10 22 23 30 40 5 12 28 38 48 21 24 29 37 47 46 -1
    // 25 20 36 10 22 30 40 5 12 28 38 48 21 24 23 29 37 47 46 -1

    tree->print();
    // tree->printLeftNodes();
    tree->printAllLeftNode();
    // tree->traverseRightItems();
    return 0;
}