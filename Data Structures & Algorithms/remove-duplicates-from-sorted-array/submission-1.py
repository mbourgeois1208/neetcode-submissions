class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums: return 0
        
        # 'slow' keeps track of where the NEXT unique number should be placed
        slow = 1 
        
        # 'fast' scans through the array starting from the second item
        for fast in range(1, len(nums)):
            
            # If we find a number that is DIFFERENT from the one right before it...
            if nums[fast] != nums[fast - 1]:
                
                # ...we copy it to the 'slow' position
                nums[slow] = nums[fast]
                
                # and move 'slow' forward by 1
                slow += 1
                
        # The problem asks us to return the number of unique elements,
        # which conveniently is exactly where our 'slow' pointer ended up!
        return slow