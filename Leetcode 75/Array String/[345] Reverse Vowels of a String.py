class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] in vowels:
                if s[high] in vowels:
                    temp = s[low]
                    s[low] = s[high]
                    s[high] = temp
                    low += 1
                    high -= 1
                else:
                    high -= 1
            else:
                low += 1
        return "".join(s)