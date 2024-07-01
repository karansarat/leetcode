class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxVol = 0
        while left < right:
            vol = min(height[left], height[right]) * (right - left)
            if vol > maxVol:
                maxVol = vol
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxVol