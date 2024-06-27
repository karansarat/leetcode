class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        zeros, ans = 1, 0
        for f in flowerbed:
            if f == 0: 
                zeros += 1
            else:
                ans += (zeros - 1) // 2
                zeros = 0
        return ans + zeros // 2 >= n 
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        