#!python3.6
#format(value[, format_spec])
v = 2**4-1
print(f'10進数値"{v}"を2,8,10,16進数で表示。')
print(format(v, 'b'))
print(format(v, 'o'))
print(format(v, 'd'))
print(format(v, 'x'))

print('スペース埋め')
print(format(123, '>8'))
print(format(123, '<8'))
print(format(123, '^8')) # 中央寄せ
print('記号埋め')
print(format(123, '=8'))
print(format(123, '#8'))
print(format(123, '08'))
