#  Write a function which takes two arguments, an array of integers and some integer N,
#  and return the pairs of integers that sum to N. 
# 
#  For example:
#  Input: [2,10,4,8,5,5,3], 7 
#  Output:[[2,5], [4,3]]
#  
#  Input: [2,10,4,8,5,5,3], 7 
#                   i  
#  Output: [[2,5], [5,2]]
#  Output: [[2,5], [4,3]] [3, 4]
#
def find_sum(arr, number):
    new_arr = [ i for i in arr if i < number ]
    new_sum = set()
    
    for i in range(len(new_arr)):
        # [ 1, 2, 3]
        for j in range(len(new_arr)):
            if i != j and (new_arr[i] + new_arr[j]) == number:
                if  [ new_arr[i], new_arr[j] ] in new_set or [ new_arr[i], new_arr[j] ][::-1] in new_set:
                    pass
                else:
                    new_sum.add([ new_arr[i], new_arr[j] ])
                # new_sum.add(sorted([ new_arr[i], new_arr[j] ]))
    
    return list(new_sum)
                
