#include <iostream>

using namespace std;

int main()
{
    int arr[2][3];
    (*(*(arr))) = 23;
    (*(*(arr+1))) = 24;
    (*(*(arr+2))) = 27;

    *(*(arr)+1) = 56;
    *(*(arr)+2) = 34;

    cout << arr[0][0] << endl;
    cout << arr[0][1] << endl;
    cout << arr[0][2] << endl;
    cout << arr[2][0] << endl;
    cout << arr[1][0] << endl;
    return 0;
}