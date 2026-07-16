class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store {number: index}
        seen = {} 
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if we've already seen the number we need
            if complement in seen:
                return [seen[complement], i]
            
            # If not, add the current number and its index to the dictionary
            seen[num] = i