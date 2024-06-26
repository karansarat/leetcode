class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> mp;
        int ma = max(s.size(), t.size());
        for(int i = 0; i < ma; i++) {
            if (i < s.size()) mp[s[i]]++;
            if (i < t.size()) mp[t[i]]--;
        }
        for(auto i:mp) {
            if (i.second != 0) return false;
        }
        return true;
    }
};