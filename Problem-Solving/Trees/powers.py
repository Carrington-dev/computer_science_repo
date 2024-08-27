
def power(number, n):
    if n == 0:
        return 1
    return number * power(number, n-1)