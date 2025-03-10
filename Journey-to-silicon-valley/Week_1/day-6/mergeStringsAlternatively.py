class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finalString = ""
        firstCount, secondCount = 0, 0
        while firstCount < len(word1) and secondCount < len(word2):
            if ((firstCount + secondCount) % 2) == 0:
                finalString += word1[firstCount]
                firstCount += 1
            if ((firstCount + secondCount) % 2) == 1:
                finalString += word2[secondCount]
                secondCount += 1
            
        
        while firstCount < len(word1):
            finalString += word1[firstCount]
            firstCount += 1

        while secondCount < len(word2):
            finalString += word2[secondCount]
            secondCount += 1

        return finalString
    

print(Solution().mergeAlternately(word1 = "abc", word2 = "pqrtvs"))