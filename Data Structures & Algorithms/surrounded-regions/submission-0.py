from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        connected = [[False for _ in range(n) ] for _ in range(m) ]

        def bfs(row,col):
            queue = deque([(row,col)])
            connected[row][col] = True

            while queue:
                r,c = queue.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr,dc in directions:
                    nr = r +dr
                    nc = c +dc
                    if 0<=nr<m and 0<=nc<n and board[nr][nc] == "O" and not connected[nr][nc]:
                        queue.append([nr,nc])
                        connected[nr][nc] = True 
        for i in range(m):
            if board[i][0] == "O" and not connected[i][0]: bfs(i,0)
            if board[i][n-1] == "O" and not connected[i][n-1]: bfs(i,n-1)
        
        for j in range(1,n-1):
            if board[0][j] == "O" and not connected[0][j]: bfs(0,j)
            if board[m-1][j] == "O" and not connected[m-1][j]: bfs(m-1,j)
        
        for k in range(1,m-1):
            for l in range(1,n-1): 
                if board[k][l] == "O" and not connected[k][l]: board[k][l] = "X"