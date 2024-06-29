class RecentCounter(object):

    def __init__(self):
        self.s = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.s and t - self.s[0] > 3000:
            self.s.pop(0)
        self.s.append(t)
        return len(self.s) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)