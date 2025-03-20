#include <iostream>

using namespace std;

int& addNumbers(int& a){
    a = a + 1;
    return a;
}

int main(){
    int c = 90;
    addNumbers(c);
    cout << c << endl;
    return 0;
}