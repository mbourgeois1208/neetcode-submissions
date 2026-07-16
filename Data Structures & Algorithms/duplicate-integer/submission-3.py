class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        for j in range(len(nums)-1): 
                if nums[j] == nums[j-1] or nums[j] == nums[j+1]: return True 
        
        return False 
            
        