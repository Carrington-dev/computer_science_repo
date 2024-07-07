#include <iostream>

using namespace std;

class  Vector{
    int allocatedSpace = 0;
    int numberOfItems = 0;
    int* data;
    public:
        Vector(){}

        void allocate(){
            if(allocatedSpace == 0){
                allocatedSpace = 1;
                data = new int[allocatedSpace];
            }else{
                allocatedSpace *= 2;
                int* myData = new int[allocatedSpace];
                for(int i = 0; i < numberOfItems; i++){
                    myData[i] = data[i];
                }
                data = myData;
            }
        }

        void insert(int value){
            if( numberOfItems < allocatedSpace){
                data[numberOfItems] = value;
            }else{
                allocate();
                data[numberOfItems] = value;
            }
            numberOfItems++;
        }

        void print(){
            for (int i = 0; i < numberOfItems; i++)
            {
                /* code */
                cout << data[i] << " " ;
            }
            cout << endl;
            
        }

        void pop(){
            numberOfItems--;
        }

        int& operator[](int item){
            if( item > numberOfItems )
            {
                cout << "Trying to access, an unexisting item " << item  << endl;
                exit(0);

            }
            
            return data[item];
        }

        ~Vector(){
            delete data;
            cout << "Deleted everything" << endl;
        }
         
};

int main(){

    Vector myDataList = Vector();
    for (int i = 0; i < 20; i++)
    {
        /* code */
        // myDataList.insert(i);
        myDataList[i] = i;
    }
    myDataList.print();
    
    return 0;
}
