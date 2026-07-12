class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        def is_valid(sub_s, l, r):
            while l < r:
                if sub_s[l] != sub_s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        while l < r:
            if s[l] != s[r]:
                return is_valid(s, l + 1, r) or is_valid(s, l, r - 1)
            l += 1
            r -= 1
        return True

