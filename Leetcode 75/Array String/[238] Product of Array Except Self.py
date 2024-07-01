class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for n in nums:
            output.append(output[-1]*n if output else n)
        right = None
        i = len(nums) - 1
        while i >= 0:
            right = right * nums[i+1] if right != None else 1
            output[i] = output[i-1] * right if i-1 >= 0 else right
            i -= 1
        return output