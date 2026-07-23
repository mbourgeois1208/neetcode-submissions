class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_volume = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            # Calculate current volume
            current_volume = min(heights[left], heights[right]) * (right - left)
            
            # Update max_volume if we found a bigger one
            if current_volume > max_volume:
                max_volume = current_volume
                
            # Move the pointer that points to the shorter line
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_volume