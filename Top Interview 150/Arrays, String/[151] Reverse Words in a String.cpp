class Solution {
public:
    string reverseWords(string s) {
        string ans = "";
        string word = "";
        int end = 0;
        int start = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != ' ') {
                start = i;
                break;
            }
        }

        for (int i = s.length() - 1; i >= start; i--) {
            if (s[i] != ' ') {
                end = i;
                break;
            }
        }

        for (int i = end; i >= start; i--) {
            if (s[i] == ' ' && word == "") {
                continue;
            } else if (s[i] == ' ' && word != "") {
                ans += word + " ";
                word = "";
            } else if (s[i] != ' ') {
                word = s[i] + word;
            }
        }
        
        ans += word;
        return ans;
    }
};