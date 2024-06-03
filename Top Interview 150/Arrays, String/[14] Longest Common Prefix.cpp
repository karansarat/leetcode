class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int len = 0;
        string prefix = "";
        for (string str : strs) {
            if (str.size() > len) len = str.size();
        }
        for (int i = 0; i < len; i++) {
            bool isCommon = true;
            for (string str : strs) {
                if (strs[0][i] != str[i]) {
                    isCommon = false;
                    break;
                }
            }
            if (isCommon) {
                prefix += strs[0][i];
            } else {
                break;
            }
        }
        return prefix;
    }
};