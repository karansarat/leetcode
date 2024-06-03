class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prevMin = prices[0];
        int sum = 0;
        for(int i = 1; i < prices.size(); ++i)
        {
            if(prices[i] < prevMin)
                prevMin = prices[i];
            else
                sum = sum < prices[i] - prevMin ? prices[i] - prevMin : sum;
        }
        return sum;
    }
};