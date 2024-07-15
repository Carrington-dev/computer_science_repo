import operator as op

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        number, string = 0, ''
        for i in range(len(s)):
            if op.contains(s[i:], s[:i]) and s[:i] != '':
                # if op.contains(s[:i], string):
                    print(s[:i].replace(string, string))
                    number, string = len(s[:i]), s[:i]
                    print(number, string)
        return string


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))