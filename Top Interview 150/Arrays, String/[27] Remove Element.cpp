class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int pos = 0;
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            if (nums[i] != val) {
               nums[pos] = nums[i];
               pos++;
            }
        }
        return pos;
    }
};