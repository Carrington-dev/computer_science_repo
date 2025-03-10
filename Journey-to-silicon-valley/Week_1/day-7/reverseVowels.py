class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
        s =  list(s)
        vowelsInString =  [i for i in s if i in vowels][::-1]
        count = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowelsInString[count]
                count += 1
        return "".join(s)


print(Solution().reverseVowels(s = "leetcode"))
print(Solution().reverseVowels(s = "IceCream"))