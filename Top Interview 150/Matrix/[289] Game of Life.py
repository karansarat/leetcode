class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 

        m = len(board)
        n = len(board[0])
        res_count = {}

        def get_neighbor_count(i,j,m,n):
            count = 0
            for row in range(i-1,i+2):
                for col in range(j-1,j+2):
                    if (i==row and j==col) or row < 0 or col < 0 or row > m-1 or col > n-1:
                        continue
                    if board[row][col] == 1:
                        count+=1
            return count

        for i in range(m):
            for j in range(n):
                count = get_neighbor_count(i,j,m,n)
                res_count[i,j] = count
        
        for i in range(m):
            for j in range(n):
                count = res_count[i,j]
                if board[i][j] == 0 and count ==3:
                    board[i][j] = 1
                elif board[i][j]==1 and (count <2 or count>3):
                    board[i][j] = 0
        
        print(res_count)