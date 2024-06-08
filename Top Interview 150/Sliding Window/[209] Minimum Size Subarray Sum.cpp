class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int result = numeric_limits<int>::max();
        int s = 0;
        int l = 0;
        for (int r = 0; r < nums.size(); r++) {
            s += nums[r];
            while (s >= target) {
                result = min(result, r + 1 - l);
                s -= nums[l++];
            }
        }
        return (result == numeric_limits<int>::max()) ? 0 : result;
    }
};