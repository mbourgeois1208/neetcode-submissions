from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # Phase 1: Setup the initial state
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c)) # Add all rotten oranges to start the wave
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # Edge Case: If there are no fresh oranges to begin with, it takes 0 minutes
        if fresh_count == 0:
            return 0
            
        # Phase 2: Multi-Source BFS (Processing in Waves)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue and fresh_count > 0:
            level_size = len(queue) # How many oranges are rotting in this specific minute?
            
            for _ in range(level_size):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is in bounds and is a fresh orange
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2       # Rot it immediately
                        fresh_count -= 1       # We have one less fresh orange
                        queue.append((nr, nc)) # Add to the queue for the next minute
                        
            # A full minute (wave) has passed
            minutes += 1 
            
        # If there are still fresh oranges left, they are unreachable
        if fresh_count > 0:
            return -1 
            
        return minutes