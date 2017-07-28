# class bytes([source[, encoding[, errors]]]) # bytearray のイミュータブル版(変更不可版)
print(bytes()) # 引数がなければ長さ 0 の配列を生成する
print(bytes(1)) # 引数が正数ならバイトサイズになる
print(bytes('a', 'utf-8')) # 引数が文字列ならencodingも与えること
