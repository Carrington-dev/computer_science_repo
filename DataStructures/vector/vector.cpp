#include <iostream>

using namespace std;

class Vector{
    int size = 0, allocated = 0;
    int *data;
    public:
        Vector(){
            data = nullptr;
        }
        void allocate(){
            if( allocated == 0){
                allocated = 1;
                data = new int[allocated];
                return;
            }else{
                allocated *= 2;
                int* newData = new int[allocated];
                for (int i = 0; i < size; i++)
                {
                    newData[i] = data[i];
                }
                data = newData;
                return;
            }
            return;      
        } 

        void insert(int value){
            if( allocated < size){
                data[size] = value;
            }
            else{
                allocate();
                data[size] = value;
            }
            size++;
            return;
        }

        int& operator[](int index){
            if( index >= size){
                throw("index is out of bounds");
                return;
            }
            return data[index];
        }

        bool operator!=(Vector* other ){
            return other != this;
        }

        bool operator==(Vector* other ){
            return other == this;
        }

        void print(){
            for (int i = 0; i < size; i++)
            {
                cout << data[i] << " ";
            }
            
        }

};

int main(){
    Vector dataList = Vector();
    for (int i = 0; i <= 20; i++)
    {
        dataList.insert(i);
    }
    dataList.print();
    cout << endl;
    for (int i = 10; i <= 21; i++)
    {
        dataList[i] = (i * 2);
    }
    dataList.print();
    cout << endl;


    
    return 0;
}