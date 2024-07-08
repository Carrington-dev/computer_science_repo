from collections import deque

queue = list()

while x := input():
    if x == -1:
        break
    
    queue.append(x)
print(queue)
while len(queue) != 0:
    print(queue.pop(0), sep=" ", end=" ")
    # print(queue.popleft(), sep=" ")

print()
print(queue)