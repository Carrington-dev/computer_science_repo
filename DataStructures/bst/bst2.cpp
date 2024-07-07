#include <iostream>

using namespace std;
class Node{
    public:
    int value;
    Node* left;
    Node* right;
    Node(int v): value(v){}
    Node(){
        left = nullptr;
        right = nullptr;
    }
};
class BinaryTree{
    public:
    Node* root;
    BinaryTree(){
        root = nullptr;
    }
    void insert(Node* subtree, int v){
        if(subtree == nullptr)
        {
            subtree == new Node(v);
            return;
        }
        if(subtree->value > v){
            insert(subtree->left, v);
        }else{
            insert(subtree->right, v);
        }
    }

    void print(Node* rt)
    {
        if(rt == nullptr)
            return;
        print(rt->left);
        cout << rt->value << " ";
        print(rt->right);
    }

    void print(){
        print(root);
    }
    void insert(int v){
        insert(root, v);
    }
};

int main(){
    BinaryTree* a;
    int c;
    c= 9;
    while( c != -1)
    {
        a->insert(c);
        cin >> c;
    }
    a->print();
    return 0;
}