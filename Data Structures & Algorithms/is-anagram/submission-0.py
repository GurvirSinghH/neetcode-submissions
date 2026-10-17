class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        t1 = Counter(t)
        
        if s1 != t1:
            return False 
        
        
        for key in s1:
            if key not in t1 or s1[key] != t1[key]:
                return False
        return True