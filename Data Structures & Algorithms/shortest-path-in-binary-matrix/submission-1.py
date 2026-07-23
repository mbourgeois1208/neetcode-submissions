from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def bfs(grid, start, goal) -> int:
            row, col = len(grid), len(grid[0])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
            
            
            queue = deque([(start[0], start[1], 0)])
            
            
            visited = set()
            visited.add((start[0], start[1]))
            
            while queue:
                print(queue)
                r, c, dist = queue.popleft() 
                
                print([r,c])
                print(goal)
                if [r, c] == goal:
                    print("yes")
                    return dist+1
                    
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0 and (nr, nc) not in visited):
                        
                        visited.add((nr, nc)) 
                        queue.append((nr, nc, dist + 1))
                        
            return -1 

        if grid[0][0] == 1: return -1 
        
        return bfs(grid,[0,0],[n-1,n-1])

        