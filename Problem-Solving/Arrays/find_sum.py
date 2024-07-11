def check_two_sum(arr, t):
    
    # Replace this placeholder return statement with your code
    # arr =  [ i for i in arr if i <= t]

    
    for i in range(len(arr)-1):
        for j in range(i, len(arr)-1):
            if arr[i] + arr[j] == t and i != j:
                return True
    return False