class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> romanToIntMap = {
            {'M', 1000}, {'D', 500}, {'C', 100}, {'L', 50}, 
            {'X', 10}, {'V', 5}, {'I', 1}
        };

        int res = 0;
        int n = s.size();
        
        for (int i = 0; i < n; ++i) {
            // If the next Roman numeral is larger, subtract the current one, otherwise add it
            if (i < n - 1 && romanToIntMap[s[i]] < romanToIntMap[s[i + 1]]) {
                res -= romanToIntMap[s[i]];
            } else {
                res += romanToIntMap[s[i]];
            }
        }

        return res;
    }
};