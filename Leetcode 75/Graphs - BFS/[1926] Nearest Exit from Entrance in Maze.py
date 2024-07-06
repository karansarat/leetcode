class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        rows, cols = len(maze), len(maze[0])
        deq = deque()
        deq.append([entr[0], entr[1], -1])
        
        while deq:
            r, c, dist = deq.popleft()
            if not (0 <= r < rows and 0 <= c < cols):
                if dist > 0:
                    return dist
                continue
            if maze[r][c] == '+':
                continue
            
            maze[r][c] = '+'
            for _r, _c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                deq.append([r + _r, c + _c, dist + 1])
        
        return -1