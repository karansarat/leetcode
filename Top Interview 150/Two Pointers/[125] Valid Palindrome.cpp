class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> str;
        str.reserve(s.size());
        for (char ch : s) {
            if (isalnum(static_cast<unsigned char>(ch))) {
                str.push_back(tolower(static_cast<unsigned char>(ch)));
            }
        }
        
        int ckpt = 0;
        int mpt = str.size() / 2;
        bool isOdd = false;
        bool isPal = true;
        if (str.size() % 2 == 0) {
            ckpt = mpt;
        } else {
            ckpt = mpt + 1;
            isOdd = true;
        }
        for (int i = ckpt; i < str.size(); i++) {
            if (isOdd) {
                if (str[i] != str[2*mpt - i]) {
                    isPal = false;
                    break;
                }
            } else {
                if (str[i] != str[2*mpt-i-1]) {
                    isPal = false;
                    break;
                }
            }
        }
        return isPal;
    }
};