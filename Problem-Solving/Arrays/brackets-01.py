class Solution:
    def isValid(self, s: str) -> bool:
        open = None
        counter = 0
        negatives = { ")", "]", "}",}
        positives = { "(", "[", "{",}
        for i in s:
            print(counter)
            if counter < 0:
                return False
            if i in negatives:
                counter -= 1
                if open == True:
                    return False
                else:
                    open = True
            if i in positives:
                counter += 1
                if open:
                    open = False
                else:
                    return False
        if counter != 0:
                return False
        
        return True