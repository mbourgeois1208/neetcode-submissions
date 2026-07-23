class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0 
        for i in range(len(heights)-1):
            for j in range(i,len(heights)):
                if i < j:
                    current_volume = min(heights[i],heights[j]) * (j-i)
                    if current_volume > max_volume: max_volume = current_volume
        
        return max_volume

        