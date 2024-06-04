class Solution {
public:
    double solve(double x, int n) {
        if (n == 0) {
            return 1;
        }
        double tmp = myPow(x, n / 2);
        if (n % 2 == 0) {
            return tmp * tmp;
        } else {
            return tmp * tmp * x;
        }
    }
    double myPow(double x, int n) {
        double res = solve(x, abs(n));
        if (n < 0) return 1 / res;
        return res;
    }
};