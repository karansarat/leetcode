class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        freq_word1 = []
        freq_word2 = []
        for ch in set(word1):
            freq_word1.append(word1.count(ch))
            count_word2 = word2.count(ch)
            freq_word2.append(count_word2)
        freq_word1.sort()
        freq_word2.sort()
        return freq_word1 == freq_word2