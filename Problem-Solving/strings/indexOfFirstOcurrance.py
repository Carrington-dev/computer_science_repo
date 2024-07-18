class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        count = 0
        while count < len(haystack):
            if (haystack[count:]).startswith(needle):
                return count
            count += 1
        return -1
    
    def strStr2(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1  

print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))
print(Solution().strStr(haystack = "saedbutsad", needle = "sad"))
print(Solution().strStr(haystack = "sadbutsad", needle = "sada"))
print(Solution().strStr(haystack = "sadbutsad", needle = ""))