class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mIdx =  min(len(word1), len(word2))
        ans = ""
        for i in range(0, mIdx):
            ans += word1[i]
            ans += word2[i]
        for i in range(mIdx, len(word1)):
            ans += word1[i]
        for i in range(mIdx, len(word2)):
            ans += word2[i]
        return ans