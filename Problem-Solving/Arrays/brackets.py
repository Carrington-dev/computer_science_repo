class Solution:
    def isNegative(self, dic):
        # print([True for i in dic.values() if i < 0])
        return [True for i in dic.values() if i < 0]

    def isValid(self, s: str) -> bool:
        negatives = { ')', ']', '}' }
        positives = { '(', '[', '{' }

        marks = {
            "]": "square",
            "[": "square",
            ")": "parenthesis",
            "(": "parenthesis",
            "}": "curly",
            "{": "curly",
        }
        is_open = {
            "square": True,
            "parenthesis": True,
            "curly": True
        }
        
        counter = {
            "square": 0,
            "parenthesis": 0,
            "curly": 0
        }
        for i in s:
            # print("s", i, is_open)
            if any(self.isNegative(counter)):
                return False
            if not any(is_open.values()):
                return False
            # if counter[marks[i]] < 0:
            #     return False
            if i in negatives:
                counter[marks[i]] -= 1
                if is_open[marks[i]]:
                    is_open[marks[i]] = False

            if i in positives:
                counter[marks[i]] += 1
                is_open[marks[i]] = True
                
        for ij in marks:
            if counter[marks[ij]] < 0 :
                return False

            if is_open[marks[i]] == False:
                return False
        
        return True
    

print(Solution().isValid('()[]{}'))
print(Solution().isValid('()'))
print(Solution().isValid('(]')) # should be false
print(Solution().isValid('([)]')) # should be invalid