s = list(range(10))
print(5 in s)
print(5 not in s)
print(s + list(range(11, 20)))
print(s * 2)
print(s[3])
#print(s[1000])#IndexError: list index out of range
print(s[3:7])
print(s[2:9:3])
print(len(s))
print(min(s))
print(max(s))
s0 = list(range(0, 100, 10))
print(s0)
print(s0.count(30))
print(s0.index(30))
print(s0.index(30, 1,2)) #ValueError: 30 is not in list

