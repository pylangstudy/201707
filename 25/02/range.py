#range(stop)
#range(start, stop[, step])
print(range(5))
for i in range(5): print(i)
print(list(range(5)))
print(*list(range(5)), sep=',')

print(range(2,5))
print(*list(range(2,5)), sep=',')

print(range(2,10,3))
print(*list(range(2,10,3)), sep=',')
