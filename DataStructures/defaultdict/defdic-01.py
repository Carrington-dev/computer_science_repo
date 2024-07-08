from collections import defaultdict, Counter

context = defaultdict(dict)

counter = Counter("Carrington")

print(counter)

for i, j in counter.items():
    context[i] = j

print(context)
print(context["Hi"])