class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        res = ''
        while True:
            if i >= len(strs[0]):
                break
            curr = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != curr:
                    return res
                curr = s[i]
            res += curr
            i += 1
        return res