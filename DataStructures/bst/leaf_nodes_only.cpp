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
        void printLeafNodes(Node* head){
            if(head == nullptr) return;
            if(head->left == nullptr && head->right == nullptr)
                cout << head->data << " ";
            printLeafNodes(head->left);
            printLeafNodes(head->right);
        }

        void print(){
            cout << "Printing With Pre-Order Traversal" << endl;
            print(root);
            cout << endl;
        }

        void insert(int data){
            insert(root, data);
        }

        void printLeafNodes(){
            cout << "Printing With printLeafNodes" << endl;
            printLeafNodes(root);
            cout << endl;
        }

        int lengthOfTree(){
            return lengthOfTree(root);
        }

        int lengthOfTree(Node* root){
            if(root == nullptr) return 0;
            return lengthOfTree(root->left) + 1 + lengthOfTree(root->right);
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

    tree->print();
    tree->printLeafNodes();
    // tree->traverseRightItems();
    cout << "Length of a tree:  " << tree->lengthOfTree() << endl;
    return 0;
}