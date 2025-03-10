class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.rstrip().lstrip().split()[::-1])
    

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
    
print(Solution().reverseWords("My name is Carrington "))
print(Solution().reverseWords("a good   example"))