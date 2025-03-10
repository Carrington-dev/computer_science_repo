#include <iostream>
#include <vector>

using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> finalNunbers =  vector<int>();
        for(int i = 0; i < nums.size(); i++){
            finalNunbers.push_back(1);
        }
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < nums.size(); j++){
                if(i != j){
                    finalNunbers[i] *= nums[j];
                }
            }
        }
        return finalNunbers;
}

int main(){

    
    return 0;
}