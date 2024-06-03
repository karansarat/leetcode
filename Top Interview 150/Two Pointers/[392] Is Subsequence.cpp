class Solution {
public:
    bool isSubsequence(string s, string t) {

    if (s.empty()) return true;

    int i = 0; // Pointer for s
    int j = 0; // Pointer for t

    while (j < t.size()) {
        if (t[j] == s[i]) {
            i++;
            if (i == s.size()) return true;
        }
        j++;
    }
    return false;
    }
};