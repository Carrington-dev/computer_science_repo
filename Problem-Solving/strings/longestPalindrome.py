class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if s[::-1] == s:
            return s
        maxed = 0
        palindromes = dict()
        for i in range(len(s)):
            for j in range(0, len(s)):
                if s[i: j] == s[i: j][::-1]:
                    if palindromes.get(len(s[i: j])) == None:
                        palindromes[len(s[i: j])] = [(s[i: j])]
                        if len(s[i: j]) > maxed:
                            maxed = len(s[i: j])
                    else:
                        if len(s[i: j]) > maxed:
                            maxed = len(s[i: j])
                        palindromes[len(s[i: j])].append([(s[i: j])])
        s = s[::-1]
        for i in range(len(s)):
            for j in range(0, len(s)):
                if s[i: j] == s[i: j][::-1]:
                    if palindromes.get(len(s[i: j])) == None:
                        palindromes[len(s[i: j])] = [(s[i: j])]
                        if len(s[i: j]) > maxed:
                            maxed = len(s[i: j])
                    else:
                        if len(s[i: j]) > maxed:
                            maxed = len(s[i: j])
                        palindromes[len(s[i: j])].append([(s[i: j])])

        return palindromes[maxed][0]

# print(Solution().longestPalindrome("babcd"))
# print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("aa"))
print(Solution().longestPalindrome("bba"))
print(Solution().longestPalindrome("abb"))
print(Solution().longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))