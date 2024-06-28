class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        def getCount(nums):
            count = {}
            for i in nums:
                if i not in count:
                    count[i] = True
            return count

        count1, count2 = getCount(nums1), getCount(nums2)

        nums1 = [i for i in count1 if i not in count2]
        nums2 = [i for i in count2 if i not in count1]

        return [nums1, nums2]
