from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        max_size = 0

        def BFS(row,col) -> int:
            queue = deque([(row,col)])
            vis[row][col] = True
            size = 1 
            while queue:
                r,c = queue.popleft()
                direction = ((1,0), (-1,0), (0,1), (0,-1))
                for dr, dc in direction:
                    nrow = r +dr
                    ncol = c +dc
                    if 0<= nrow< m and 0<=ncol<n and not vis[nrow][ncol] and grid[nrow][ncol] == 1:
                        vis[nrow][ncol] = True 
                        queue.append([nrow,ncol])
                        size += 1
            return size 
        
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 1 and not vis[i][j]:
                    
                    size = BFS(i,j)
                    if size > max_size: max_size = size
                    print(max_size)
        
        return max_size 
            
