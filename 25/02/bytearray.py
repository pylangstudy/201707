# class bytearray([source[, encoding[, errors]]])
print(bytearray()) # 引数がなければ長さ 0 の配列を生成する
print(bytearray(1)) # 引数が正数ならバイトサイズになる
print(bytearray('a', 'utf-8')) # 引数が文字列ならencodingも与えること
