class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans=[0]
        for i in range(len(gain)):
            ans.append(ans[i] + gain[i])            
        return max(ans)