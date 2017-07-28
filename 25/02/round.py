#!python3.6
#round(number[, ndigits])
#たしかPythonバージョンごとに動作が異なっていたはず。
# * python2だと四捨五入
# * python3だと偶数側に丸める
print(round(-3.5)) #-4
print(round(-3.4)) #-3
print(round(-2.5)) #-2
print(round(-2.4)) #-2
print(round(-1.5)) #-2
print(round(-1.4)) #-1
print(round(0.4)) #0
print(round(0.5)) #0
print(round(1.4)) #1
print(round(1.5)) #2
print(round(2.4)) #2
print(round(2.5)) #2
print(round(3.4)) #3
print(round(3.5)) #4
print(round(4.4)) #4
print(round(4.5)) #4
