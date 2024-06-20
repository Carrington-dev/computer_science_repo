In C++, hash maps are commonly implemented using the `std::unordered_map` container provided by the Standard Library. The runtime complexity of operations on `std::unordered_map` depends on several factors, including the quality of the hash function, the load factor, and how evenly the hash function distributes elements across the buckets.

### Average Case Complexity
1. **Insertion:** O(1)
2. **Lookup:** O(1)
3. **Deletion:** O(1)

### Worst Case Complexity
1. **Insertion:** O(n)
2. **Lookup:** O(n)
3. **Deletion:** O(n)

The worst-case complexity occurs when all elements hash to the same bucket, leading to a linear search within that bucket. However, with a good hash function and a well-chosen load factor, the average case is typically achieved.

### Factors Affecting Runtime
1. **Hash Function:** A good hash function minimizes collisions and ensures a uniform distribution of keys across buckets.
2. **Load Factor:** This is the ratio of the number of elements to the number of buckets. The `std::unordered_map` typically performs rehashing to maintain a low load factor (commonly around 1.0) to ensure efficient performance.
3. **Rehashing:** When the number of elements exceeds the load factor threshold, the hash map may rehash, which involves creating a new set of buckets and redistributing the elements. This can lead to occasional O(n) operations, but it helps maintain the average O(1) complexity for insertions, lookups, and deletions.

### Example Usage
Here's a simple example demonstrating the use of `std::unordered_map` in C++:

```cpp
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
```

### Conclusion
The `std::unordered_map` provides an efficient hash map implementation in C++ with average-case constant time complexity for insertions, lookups, and deletions. However, it is important to be aware of the factors that can affect its performance, such as the quality of the hash function and the load factor.