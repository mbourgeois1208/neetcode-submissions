class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i+1]-nums[i] != 1: return nums[i]+1
        
        if nums[0]!= 0: return 0 
        if nums[0]!= n: return n
        
         
        