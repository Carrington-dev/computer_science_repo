from collections import defaultdict

context =  defaultdict()

print(context)

d = defaultdict(list)

for i in range(5):
    d[i].append(i)
    
print("Dictionary with values as list:")
print(d)