class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for idx in range(len(haystack)):
            if haystack[idx] == needle[0]:
                if haystack[idx: idx+ len(needle)] == needle:
                    return idx
