class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        sup = [1]
        for i in range(len(digits)):
            if digits[n-1-i] < 9: 
                digits[n-1-i] += 1
                return digits
            else:
                digits[n-1-i] = 0
                if i == n-1:
                    digits = sup + digits

        return digits