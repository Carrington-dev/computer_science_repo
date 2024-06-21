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

        void childOrderTraversal(){
            childOrderTraversal(root);
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


        void childOrderTraversal(Node* root){
            if( root == nullptr) return;
            queue<Node*> queue;
            queue.push(root);

            while( !queue.empty() ){
                Node* consideredNode = queue.front();
                
                cout << consideredNode->data << " ";
                queue.pop();

                if( consideredNode->left != nullptr){
                    queue.push(consideredNode->left);
                }
                if( consideredNode->right != nullptr){
                    queue.push(consideredNode->right);
                }
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

    cout << "preOrderTraversal" << endl;
    myList->preOrderTraversal();
    cout << "childOrderTraversal" << endl;
    myList->childOrderTraversal();
    cout << "postOrderTraversal" << endl;
    myList->postOrderTraversal();
    // myList->lowOrderTraversal();
    // myList->levelTreeOrderTraversal();
    // cout << "Height: " << myList->heightOfTree() << endl;
    // cout << "Length: " << myList->lengthOfTree() << endl;
    return 0;
}