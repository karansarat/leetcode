class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp, dpPrev = [0] * (n+1), [0] * (n+1)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[j] = dpPrev[j-1] + 1
                else:
                    dp[j] = max(dp[j-1], dpPrev[j])
            dp, dpPrev = dpPrev, dp
        return dpPrev[n]