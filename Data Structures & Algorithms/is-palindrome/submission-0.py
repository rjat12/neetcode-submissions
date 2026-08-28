class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(c for c in s if c.isalnum())
        for i in range(len(s1)//2):
            if s1[i].lower() != s1[(len(s1)-1)-i].lower():
                return False
        return True
        