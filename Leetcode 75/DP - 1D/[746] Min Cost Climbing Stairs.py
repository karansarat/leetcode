class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1] , dp[-2])
