def check_two_sum(arr, t):
    
    # Replace this placeholder return statement with your code
    context = { i:i for i in arr }

    
    for i in range(len(arr)-1):
       if (t - i) in context:
                return True
    return False

def find_sum_of_two(A, val):
  found_values = set()
  for a in A:
    if val - a in found_values:
      return True

    found_values.add(a)
    
  return False

v = [5, 7, 1, 2, 8, 4, 3]
test = [3, 20, 1, 2, 7]

for i in range(len(test)):
  output = find_sum_of_two(v, test[i])
  print("find_sum_of_two(v, " + str(test[i]) + ") = " + str(output))