class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0;
        int end = height.size() - 1;
        int maxWater = 0;

        while (start < end) {
            int h = min(height[start], height[end]);
            int currWater = h * (end - start);
            if (currWater > maxWater) maxWater = currWater;
            if (height[start] < height[end]) start++;
            else end--;
        }
        return maxWater;
    }
};