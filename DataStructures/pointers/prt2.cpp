#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int* run = new int[5];
    int* b = run;
    *(run + 1) = 2;
    cout << "run = " << *(run+1) << endl;
    cout << "b   = " << *(b+2) << endl;

    *b = 67;
    cout << "_______________________" << endl;
    cout << "run = " << *run << endl;
    cout << "b   = " << *b << endl;

    *run = 45;
    cout << "_______________________" << endl;
    cout << "run = " << *run << endl;
    cout << "b   = " << *b << endl;
    vector<vector<char>> v;
    vector<char> tmp(5, 'a');
    v.push_back(tmp);

    v.emplace_back(5, 'b');
    cout << "_______________________" << endl;
    
    cout << v[0].size() << endl;

    for(size_t i = 0; i < v.size(); i++)
    {
        for(size_t j = 0; j < v[i].size(); j++)
        {

            cout << v[i][j] << " " << i << " " << j << endl;
        }
    }

    return 0;
}