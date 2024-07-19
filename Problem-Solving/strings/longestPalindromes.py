class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s)
        maxed = 0
        context = {}
        while left <= right:
            if s[:right] == s[:right][::-1]:
                if maxed < len(s[:right]):
                    maxed = len(s[:right])
                if context.get(len( s[: right])) == None:
                    context[len(s[: right])] = [ s[: right] ]
                else:
                    context[len(s[: right])].append( s[: right] )

            if s[left:] == s[left:][::-1]:
                if maxed < len(s[left:]):
                    maxed = len(s[left:])
                if context.get(len( s[left: ])) == None:
                    context[len(s[left: ])] = [ s[left: ] ]
                else:
                    context[len(s[left: ])].append( s[left: ] )

            if s[left: right] == s[left: right][::-1] != "":
                if context.get(len( s[left: right])) == None:
                    context[len(s[left: right])] = [ s[left: right] ]
                else:
                    context[len(s[left: right])].append( s[left: right] )
                if maxed < len(s[left: right]):
                    maxed = len(s[left: right])


            left += 1
            right -= 1
        print(context)
        return context[maxed][0]



print(Solution().longestPalindrome(s = "babad"))
print(Solution().longestPalindrome(s = "cbbd"))
print(Solution().longestPalindrome(s = "ac"))
print(Solution().longestPalindrome(s = "abb"))
print(Solution().longestPalindrome(s = "ccd"))
print(Solution().longestPalindrome(s = "aacabdkacaa"))