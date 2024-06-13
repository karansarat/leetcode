class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    self.dfs(x, y, m, n, grid)
                    count += 1
        return count
    def dfs(self, x, y, m, n, grid):
        if x >= m or x < 0 or y >= n or y < 0 or grid[x][y] == "0":
            return False
        grid[x][y] = "0"
        self.dfs(x, y+1, m, n, grid)
        self.dfs(x+1, y, m, n, grid)
        self.dfs(x, y-1, m, n, grid)
        self.dfs(x-1, y, m, n, grid)
        return True