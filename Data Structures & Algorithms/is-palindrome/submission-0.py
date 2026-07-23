class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = "".join(char.lower() for char in s if char.isalnum())
        n = len(clean)
        for i in range(n//2):
            print(clean[i])
            if clean[i] != clean[n-1-i]:return False
        
        return True
        