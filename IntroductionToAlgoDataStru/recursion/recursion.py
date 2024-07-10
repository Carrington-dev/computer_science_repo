def reverse_string(string):
    if len(string) <= 1:
        return string
    if len(string) == 2:
        return string[1] + string[0]
    return reverse_string(string[2:]) + reverse_string(string[:2])

print(reverse_string("Carrington"))
print(reverse_string("Carrington")[::-1])


def power(number, n):
    if n == 0:
        return 1
    return number * power(number, n-1)


print(power(10, 0))
print(power(10, 1))
print(power(10, 2))
print(power(10, 10))