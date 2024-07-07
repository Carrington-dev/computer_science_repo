    #include <iostream>

    using namespace std;

    class TreeNode{
    public:
        // Pointer to the left child
        //  Initialised to nullptr (this syntax is a new C++11 feature)
        TreeNode* left = nullptr;
        // Pointer to the right child
        //  Initialised to nullptr (this syntax is a new C++11 feature)
        TreeNode* right = nullptr;

        // Value in the node
        int value;

        // Constructor, sets the value
        TreeNode(int v) : value(v) {}
        // Destructor, nifty trick to recursively delete all the nodes
        //  be careful though, when you delete just a single node, make
        //  sure that you set left and right = nullptr first
        ~TreeNode() {
            delete left;
            delete right;
        }
    };

    class Tree{
    private:
        TreeNode* root = nullptr;

    public:
        // These functions do the actual work
        void insert(int v, TreeNode* &subtree){
            if(subtree == nullptr){
            subtree = new TreeNode(v);
            }else if(v < subtree->value){
                insert(v, subtree->left);
            }else{
                insert(v, subtree->right);
            }
        }

        void preOrderTraversal(TreeNode* subtree) const{

            if(subtree == NULL)
                return;
            
            cout << subtree->value << " ";
            preOrderTraversal(subtree->left);
            preOrderTraversal(subtree->right);

        }

        void inOrderTraversal(TreeNode* subtree) const{
            if(subtree == NULL)
                return;
            
            inOrderTraversal(subtree->left);
            cout << subtree->value << " ";
            inOrderTraversal(subtree->right);
        }

        void postOrderTraversal(TreeNode* subtree) const{
            if(subtree == NULL)
                return;
            
            postOrderTraversal(subtree->left);
            postOrderTraversal(subtree->right);
            cout << subtree->value << " ";
        }

        int min(TreeNode* subtree) const{
            if(subtree == NULL)
                return subtree->value;
            
        
            TreeNode* current = subtree;
            while(current->left != NULL)
            {
                current = current->left;
            }
            return (current->value);
            
        }
        int max(TreeNode* subtree) const{
            if(subtree == NULL)
                return -1;
            
            
            TreeNode* current = subtree;
            while(current->right != NULL)
            {
                current = current->right;
            }
            return current->value;
        }
        bool contains(int value, TreeNode* subtree) const{
            if(subtree == NULL)
                return false;

            int co = subtree->value;
            
            if(value == co)
            {
                return true;
            }
            bool is = contains(value, subtree->left);
            bool isr = contains(value, subtree->right);
            if(is) return true;
            if(isr) return true;
            return false;
        }

        void remove(int value, TreeNode* &subtree){
            // base case
            if(contains(value))
            {
                if (subtree == NULL)
                    return ;
                TreeNode* current = subtree;
                TreeNode* prev = nullptr;
                if(value < current->value)
                {
                    while(current->left != NULL && current->value != value)
                    {
                        prev = current;
                        current = current->left;
                    }
                    prev->left = current->left;
                    
                    
                }
            }
   
            // if (value > subtree->value)
            //     remove(value, subtree->left);
            
            // if (value < subtree->value)
            //     remove(value, subtree->right);
            
           return;
           
        }

        void insert(int value){
            insert(value, root);
        }

        void preOrderTraversal(){
            preOrderTraversal(root);
            cout << endl;
        }
        void inOrderTraversal(){
            inOrderTraversal(root);
            cout << endl;
        }
        void postOrderTraversal(){
            postOrderTraversal(root);
            cout << endl;
        }
        int min(){
            return min(root);
        }
        int max(){
            return max(root);
        }
        bool contains(int value){
            return contains(value, root);
        }
        void remove(int value){
            remove(value, root);
        }
        ~Tree(){
            // This ends up deleting all the nodes recursively.
            delete root;
        }
    };

    int main(){
        Tree t;
        int value;
        // Sample code to read and construct the tree.
        while(cin >> value && value != -1){
            t.insert(value);
        }
        
        int test;
        while(cin >> test && test != -1){
            // t.insert(value);
            t.remove(test);
            t.preOrderTraversal();
            t.inOrderTraversal();
            t.postOrderTraversal();
            cout << endl;
        }
        
    }
