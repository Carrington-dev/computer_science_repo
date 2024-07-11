def find_missing(nums):
  
    # Replace this placeholder return statement with your code
    n = len(nums) + 1
    print(sum(list(range(1, n))))
    return sum(list(range(1, n+1))) - sum(nums)


print(find_missing([3, 7, 1, 2, 8, 4, 5]))