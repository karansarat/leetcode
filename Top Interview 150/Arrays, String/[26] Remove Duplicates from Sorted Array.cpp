class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int num = nums[0];
        int pos = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != num) {
                num = nums[i];
                nums[pos] = num;
                pos++;
            }
        }
        return pos;
    }
};