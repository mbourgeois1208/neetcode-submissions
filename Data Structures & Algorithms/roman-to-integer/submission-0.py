class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0 
        delta = 0 
        max_delta = 0 
        n = len(s)

        for i in range(len(s)):
            a = s[n-1-i]
            if a =="I": delta =  1
            elif a =="V": delta =  5
            elif a =="X": delta =  10
            elif a =="L": delta =  50
            elif a =="C": delta =  100
            elif a =="D": delta =  500
            elif a =="M": delta =  1000
            if delta < max_delta: delta = -1*delta
            elif delta > max_delta: max_delta = delta 
            number += delta
        
        return number