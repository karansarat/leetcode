class Solution {
public:
    int lengthOfLastWord(string s) {
        vector<char> str(s.begin(), s.end());
        int endPos = 0;
        int startPos = 0;
        
        //if (str.size() == 1 && str[0] != ' ') return 1;

        for (int i = 1; i <= str.size(); i++) {
            if (str[str.size() - i] != ' ') {
                endPos = str.size() - i;
                break;
            }
        }
        for (int i = 1; i <= endPos; i++) {
            if (str[endPos - i] == ' ') {
                startPos = endPos - i;
                break;
            }
        }
        if (startPos == 0 && str[0] != ' ') startPos = -1;
        return endPos - startPos;
    }
};