from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        allChars = set(words[0])
        for i in words:
            for j in i:
                if i in allChars:
                    # allChars.pop(j)
                    print(j)
        return allChars

print(Solution().commonChars(words = ["bella","label","roller"]))
print(Solution().commonChars(words = ["cool","lock","cook"]))

"""
["bella","label","roller"]


"""