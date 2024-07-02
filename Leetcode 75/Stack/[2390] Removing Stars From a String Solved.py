class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for ch in s:
            stack.append(ch)
            if stack[-1] == "*":
                stack.pop()
                if stack: stack.pop()
        
        return "".join(stack)