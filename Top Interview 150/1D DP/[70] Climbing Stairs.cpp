class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        vector<int> graph(n+1);
        for (int i = 0; i <= n; i++) {
            if (i <= 2) {
                graph[i] = i;
                continue;
            }
            graph[i] = graph[i-1] + graph[i-2];
        }
        return graph[n];
    }
};