class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int stations = gas.size();
        int totalCost = 0;
        int totalGas = 0;
        int start = 0;
        int currGas = 0;
        for (int i = 0;  i < stations; i++) {
            totalCost += cost[i];
            totalGas += gas[i];
        }
        if (totalCost > totalGas) return -1;
        for (int i = 0; i < stations; i++) {
            if (currGas < 0) {
                currGas = 0;
                start = i;
            }
            currGas += gas[i] - cost[i];
        }
        return start;
    }
};