class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        long long reversed = 0;
        long long tmp = x;

        while (tmp != 0) {
            int digit = tmp % 10;
            reversed = reversed * 10 + digit;
            tmp /= 10;
        }

        return (reversed == x);
    }
};