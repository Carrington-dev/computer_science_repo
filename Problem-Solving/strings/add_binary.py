class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            new_string = "0"* (len(a) + 1)
        else:
            new_string = "0"* (len(b) + 1)
        
        a = "0" * abs(len(new_string) - len(a)) + a
        b = "0" * abs(len(new_string) - len(b)) + b

        counter = 1
        new_string = [ i for i in new_string]
        while counter < len(new_string):
            print(new_string)
            if (a[-1* counter ]) == "1" and ( b[-1 * counter] ) == "1":
                new_string[ -1 * counter ] = "0"
                new_string[-1 * counter - 1] = "1"
            if ((a[-1*counter]) == "1" or (b[-1*counter]) == "1"):
                new_string[ -1 * counter ] = "1"
            else:
                new_string[ -1 * counter ] = "0"
            counter += 1
        
        while new_string[0] == "0":
            new_string.pop(0)
        return "".join(new_string)
    
# print(Solution().addBinary("00101", "100"))
print(Solution().addBinary("101", "100"))
# print(Solution().addBinary("0101", "100"))