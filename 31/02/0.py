def my_generator():
    yield 1
    yield 2
    yield 3

for v in my_generator(): print(v)
