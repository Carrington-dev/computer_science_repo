def infiniteNumbers():
    num = 1
    while True:
        yield num
        num += 1

gen = infiniteNumbers()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# https://yasirbhutta.github.io/python/posts/generators-in-python.html