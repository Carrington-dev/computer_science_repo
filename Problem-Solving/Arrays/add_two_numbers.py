from typing import List


class Solution:
    def addTwoNumbers(self, digits_one: List[int], digits_two: List[int]) -> List[int]:
        # print("digits_one", digits_one, " digits_two ", digits_two)
        isSolved = False
        diff  = abs(len( digits_one)  - len(digits_two))
        if len( digits_one)  == len(digits_two):
            new_digits = [ 0 ] + [ 0 for i in range(len(digits_one))]
        elif len( digits_one)  > len(digits_two):
            new_digits = [ 0 ] + [ 0 for i in range(len(digits_one))]
            digits_two = [ 0 for i in range(diff) ] + digits_two
        else:
            new_digits = [ 0 ] + [ 0 for i in range(len(digits_two))]
            digits_one = [ 0 for i in range(diff) ] + digits_one


        counter = 1
        while not isSolved:
            
            if digits_two[-1 * counter] + digits_one[-1 * counter]  <= 9:
                # new_digits[ -1 * counter] += digits_two[-1 * counter] + digits_one[-1 * counter]
                new_digits[ -1 * counter] += (digits_two[-1 * counter] + digits_one[-1 * counter]) % 10
                new_digits[ -1 * (counter + 1)] += (digits_two[-1 * counter] + digits_one[-1 * counter]) // 10
            else:
                new_digits[ -1 * counter] += (digits_two[-1 * counter] + digits_one[-1 * counter]) % 10
                new_digits[ -1 * (counter + 1)] += (digits_two[-1 * counter] + digits_one[-1 * counter]) // 10
            counter += 1
            if counter == len(new_digits):
                isSolved  = True
        

        counter = len(new_digits) - 1
        while counter >= 0:
            if new_digits[counter] >= 10:
                new_digits[counter] =  new_digits[counter] % 10
                new_digits[counter-1] += 1
            counter -= 1
        while new_digits[0] == 0:
            new_digits.pop(0)
        return new_digits
    


print(Solution().addTwoNumbers([1, 0], [2, 3]))
print(Solution().addTwoNumbers([0, 1, 9], [6, 2, 3]))
print(Solution().addTwoNumbers([0, 1, 9], [6, 2, 1]))
print(Solution().addTwoNumbers([0, 0, 1, 9], [0, 6, 2, 1]))
print(Solution().addTwoNumbers([0, 0, 0, 0, 1, 9], [0, 6, 2, 1]))
print(Solution().addTwoNumbers([0, 0, 9, 9, 1, 9], [0, 6, 2, 1]))
print(Solution().addTwoNumbers([0, 10, 9, 9, 1, 9], [0, 6, 2, 1]))