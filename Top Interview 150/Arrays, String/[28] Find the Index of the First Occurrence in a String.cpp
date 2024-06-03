class Solution {
public:
    int strStr(string haystack, string needle) {
        vector<char> hstr(haystack.begin(), haystack.end());
        vector<char> nstr(needle.begin(), needle.end());

        if (haystack == needle) {
            return 0;
        }
        if (nstr.size() > hstr.size()) {
            return -1;
        }
        
        for (int i=0; i < hstr.size() - nstr.size() + 1; i++) {
            bool isFound = false;
            if (hstr[i] == nstr[0]) {
                if (nstr.size() == 1) return i;
                isFound = true;
                for (int j = 1; j < nstr.size(); j++) {
                    if (nstr[j] != hstr[i+j]) {
                        isFound = false;
                        break;
                    }
                }
            }
            if (isFound) {
                return i;
            }
        }
        return -1;
    }
};