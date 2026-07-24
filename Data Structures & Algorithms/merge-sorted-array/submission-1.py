class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Pointers for the last actual numbers in nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        
        # Pointer for the very end of nums1 (the last zero)
        p = m + n - 1
        
        # While there are still numbers in nums2 to merge
        while p2 >= 0:
            # If nums1 still has numbers, and its number is bigger
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Otherwise, the number in nums2 is bigger (or equal)
                nums1[p] = nums2[p2]
                p2 -= 1
                
            # Move the placement pointer back one step
            p -= 1