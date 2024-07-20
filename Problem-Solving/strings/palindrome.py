

class Solution:
    def isPalindrome(self, s: str) -> bool:

        a = "0123456789abcdefghijklmnopqrstuvwxyz" 
        a += a.upper()
        w = ""
        for i in s.lower():
            if i in a:
                w += i.lower()
        return w == w[::-1]

print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))
print(Solution().isPalindrome(s = "0P"))