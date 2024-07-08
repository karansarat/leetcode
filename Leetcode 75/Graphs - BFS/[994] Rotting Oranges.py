class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visit, curr = set(), []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))
        result = 0
        while visit and curr: 
            newr = []
            for i, j in curr:
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in visit:
                        visit.remove(coord)
                        newr.append(coord)
            curr = newr
            result += 1
        return -1 if visit else result
