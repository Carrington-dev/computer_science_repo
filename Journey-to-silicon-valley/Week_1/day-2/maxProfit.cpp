#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            int buyingPrice = prices[0];
            int profit = 0;

            for (size_t i = 0; i < prices.size(); i++)
            {
                if(buyingPrice > prices[i]){
                    buyingPrice = prices[i];
                }

                if(profit < prices[i] - buyingPrice ){
                    profit = prices[i] - buyingPrice;
                }
            }
            return profit;
            

        }
    };