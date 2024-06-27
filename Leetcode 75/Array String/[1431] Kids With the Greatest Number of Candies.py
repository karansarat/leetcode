"""
:type candies: List[int]
:type extraCandies: int
:rtype: List[bool]
"""
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
		high_enough = max(candies) - extraCandies
		result = []
		for num in candies:
			result.append(num >= high_enough)
		return result