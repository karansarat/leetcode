class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        transpose = Counter(zip(*grid))
        grid = Counter(map(tuple,grid)) 
        return  sum(transpose[t] * grid[t] for t in transpose) 