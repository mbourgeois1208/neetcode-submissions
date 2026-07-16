from collections import deque 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        vis_pacific = [[False for _ in range(n)] for _ in range(m)]
        vis_atlantic = [[False for _ in range(n)] for _ in range(m)]

        def BFS(row,col,sea): 
            queue = deque([(row,col)])
            if sea == 3: vis = vis_pacific
            else: vis = vis_atlantic 
            vis[row][col] = True 
            while queue:
                r,c = queue.popleft()
                directions = ((1,0), (-1,0), (0,1),(0,-1))
                for dr,dc in directions:
                    nrow = dr + r 
                    ncol = dc + c 
                    if 0<= nrow < m and 0<= ncol <n and not vis[nrow][ncol] and heights[nrow][ncol] >= heights[r][c]: 
                        vis[nrow][ncol] = True 
                        queue.append((nrow,ncol))
        

        for i in range(m):
            if not vis_pacific[i][0]: BFS(i,0,3)
            if not vis_atlantic[i][n-1]: BFS(i,n-1,4)
        
        for j in range(n):
            if not vis_pacific[0][j]: BFS(0,j,3)
            if not vis_atlantic[m-1][j]: BFS(m-1,j,4)
        
        liste= []
        for i in range(m):
            for j in range(n):
                if vis_pacific[i][j] and vis_atlantic[i][j]: 
                    liste.append([i,j])
        
        return liste 
        