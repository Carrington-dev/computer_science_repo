#include <iostream>

using namespace std;

int main()
{
    int* p = nullptr;
    char* q = nullptr;
    for(int i = 0; i < 5; i++)
    {
        p = new int(i);
        q = new char(i);
        cout << *p << endl;
        cout << *q << endl;
    }
    return 0;
}