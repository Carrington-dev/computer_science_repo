#include <iostream>
#include <map>
#include <utility>

using namespace std;

string generateUUID(){
    return "";
}

int main(){
    map<string, string> names;

    names.insert(make_pair("Carrington", "Muleya"));
    names.insert(make_pair("Mulalo", "Mulaudzi"));
    names.insert(make_pair("Mpho", "Ndou"));
    names.insert(make_pair("Portia", "Muleya"));
    names.insert(make_pair("Precious", "Muleya"));
    names.insert(make_pair("Shae", "Mudau"));
    names.insert(make_pair("Avhurengwi", "Sivhali"));

    for( auto item: names){
        cout << "Name: " << item.first << ", Surname: " << item.second << endl;
    }

    bool isPresent = names.find("Mulalo") != names.end();
    if (isPresent)
    {
        cout << "Mulalo is present" << endl;
    }
    

    system("pause>0");
    return 0;
}