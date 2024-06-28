class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum, rightSum = 0, sum(nums)
        
        for i, v in enumerate(nums):
            rightSum -= v
            if leftSum == rightSum:
                return i
            leftSum += v
            
        return -1
