import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        
        for x, y in points:
            dist = (x**2 + y**2)
            # Python only has min-heaps, so we push negative distances to simulate a max-heap
            heapq.heappush(max_heap, (-dist, x, y))
            
            # If our heap gets bigger than k, pop the largest distance out
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # Extract the remaining coordinates from the heap
        return [[x, y] for (dist, x, y) in max_heap]