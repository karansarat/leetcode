class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] + a < 0: stack.pop()
                elif stack[-1] + a > 0: break    
                else: stack.pop(); break
            else: stack.append(a)        
        return stack