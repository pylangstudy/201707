import math
print(math.trunc(3.14))
print(math.trunc(7.89))
print('----- round(x) -----')
for i in range(10): print(i, round(i+0.5), i+0.5)
print('----- round(x, 1) -----')
for i in range(10): print(i, round((i*0.1)+0.05, 1), (i*0.1)+0.05) # 浮動小数点の誤差がある
print('----- math.floor -----')
for i in range(10): print(i, math.floor(i+0.5), i+0.5)
print('----- math.ceil -----')
for i in range(10): print(i, math.ceil(i+0.5), i+0.5)
