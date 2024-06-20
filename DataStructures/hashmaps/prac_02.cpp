#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<int, std::string> myMap;

    // Insertion
    myMap[1] = "one";
    myMap[2] = "two";
    myMap[3] = "three";

    // Lookup
    if (myMap.find(2) != myMap.end()) {
        std::cout << "Key 2 is found with value: " << myMap[2] << std::endl;
    } else {
        std::cout << "Key 2 is not found." << std::endl;
    }

    // Deletion
    myMap.erase(2);

    if (myMap.find(2) != myMap.end()) {
        std::cout << "Key 2 is found with value: " << myMap[2] << std::endl;
    } else {
        std::cout << "Key 2 is not found." << std::endl;
    }

    return 0;
}
