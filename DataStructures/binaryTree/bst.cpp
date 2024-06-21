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
        void lowOrderTraversal(Node* root){
            if(root == nullptr) return;
            lowOrderTraversal(root ->right);
            cout << root -> data << " ";
            lowOrderTraversal(root ->left);
        }
        void lowOrderTraversal(){
            lowOrderTraversal(root);
            cout << endl;
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

        int heightOfTree(Node* root, int length = 0){
            if(root == nullptr) return length;
            return heightOfTree(root -> left, length + 1);
        }

        int heightOfTree(){
            return heightOfTree(root, 0);
        }

        int lengthOfTree(){
            return heightOfTree(root, 0) + heightOfTree(root->right, 0);
        }
        void levelTreeOrderTraversal(){
            levelTreeOrderTraversal(root);
            cout << endl;
        }

        void levelTreeOrderTraversal(Node* root){
            if( root == nullptr) return;
            queue<Node*> queue;
            queue.push(root);

            while( !queue.empty() ){
                Node* printedNode = queue.front();
                cout << printedNode->data << " ";
                queue.pop();

                if ( root->left != nullptr)
                {
                    queue.push(printedNode->left);
                }
                if ( root->right != nullptr)
                {
                    queue.push(printedNode->right);
                }
                
                // levelTreeOrderTraversal(root -> left);
                // levelTreeOrderTraversal(root -> right);
            }


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

    // myList->preOrderTraversal();
    myList->inOrderTraversal();
    // myList->postOrderTraversal();
    // myList->lowOrderTraversal();
    myList->levelTreeOrderTraversal();
    cout << "Height: " << myList->heightOfTree() << endl;
    cout << "Length: " << myList->lengthOfTree() << endl;
    return 0;
}