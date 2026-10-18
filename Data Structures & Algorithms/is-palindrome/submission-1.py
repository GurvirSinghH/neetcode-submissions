class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(c for c in s if c.isalnum())
        s1 = s1.lower()
        s2 = s1[::-1]
        return True if s1 == s2 else False