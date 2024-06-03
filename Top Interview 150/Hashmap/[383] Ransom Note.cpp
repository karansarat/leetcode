class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> n(26, 0);
        for (const auto& i : magazine) {
            ++n[i - 'a'];
        }
        for (const auto& i : ransomNote) {
            --n[i - 'a'];
        }
        for (const auto& i : n) {
            if (i < 0) {
                return false;
            }
        }
        return true;
    }
};
