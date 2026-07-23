class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        
        # Dictionary to store {past_running_totals: frequency}
        # We start with {0: 1} to account for a subarray that starts exactly at index 0.
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # If we chop off a previous sum (current_sum - k), does it leave exactly k?
            diff = current_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
            
            # Add the current sum to our dictionary for future numbers to use
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count