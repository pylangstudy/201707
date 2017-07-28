#!python3.6
#round(number[, ndigits])
#たしかPythonバージョンごとに動作が異なっていたはず。
# * python2だと四捨五入
# * python3だと偶数側に丸める
#https://docs.python.jp/3/library/functions.html#round
# * 浮動小数点数で正確に表せないため誤差が生じる
#     * 少数第n位の丸めは正確にできない（浮動小数点数の場合）
print(round(2.50, 0)) #2.0
print(round(2.51, 0)) #3.0
print(round(2.61, 1)) #2.6
print(round(2.65, 1)) #2.6  予想外。2.7になると思った。浮動小数点の誤差。
print(round(2.66, 1)) #2.7
print(round(2.675, 1)) #2.7
print(round(2.675, 2)) #2.67  予想外。2.68になると思った。浮動小数点の誤差。
