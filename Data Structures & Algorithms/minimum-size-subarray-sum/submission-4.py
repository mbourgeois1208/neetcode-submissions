class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        min_length = n + 1
        
        total = 0
        left = 0 # This tracks the back of our window
        
        # 'right' tracks the front of our window
        for right in range(n):
            total += nums[right]
            
            # When we hit the target, we trigger the shrinking process
            while total >= target:
                # Record the current window size if it's the smallest we've seen
                window_size = right - left + 1
                if window_size < min_length:
                    min_length = window_size
                
                # Chop off the left-most number to shrink the window
                total -= nums[left]
                left += 1
                
        # If min_length never changed, we never hit the target
        if min_length == n + 1:
            return 0
        else:
            return min_length