#include <iostream>
#include <vector>

using namespace std;

struct Thing{
    vector<vector<char>> v;
    static int w;
    int x, y, z;

    Thing Tile() : x(1), y(2), z(3) {
        w++;
        
        vector<char> tmp(5, 'a');
        v.push_back(tmp);

        v.emplace_back(5, 'b');
        }
    };
    int Tile::w = 0;

    int main(){
    Thing t;

    int x = t.x;
    int &y = t.y;
    int *z = &t.z;

    cout << "w = " << t.w << ",x = " << x
    << ",y = " << y << ",z = " << *z << endl;

    t.x = 42; t.y = 15; t.z = 38;

    Thing unused_thing;

    cout << "w = " << t.w << ",x = " << x
    << ",y = " << y << ",z = " << *z << endl;

    cout << "size = [" << t.v.size()
    << "," << t.v[0].size() << "]" << endl;

    cout << "v[0][0] = " << t.v[0][0]
    << ",v[0][1] = " << t.v[0][1] << endl;
}
