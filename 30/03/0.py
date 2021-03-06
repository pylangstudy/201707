print('1, 2, 3 = {0:#b}, {1:#b}, {2:#b}'.format(1, 2, 3))
print('1 | 2 = {}'.format(1 | 2));
print('1 & 2 = {}'.format(1 & 2));
print('1 ^ 3 = {}'.format(1 ^ 3));
print('2<<8 =', 2<<8)
print('255>>2 =', 255>>2)
# short, int, longのように精度制限がないから10進数表記だと符号反転になる
print('~1', ~1, bin(~1))
print('~-1', ~-1, bin(~-1))
print('~2', ~2, bin(~2))
print('~-2', ~-2, bin(~-2))
print('~3', ~3, bin(~3))
print('~-3', ~-3, bin(~-3))

# どうしても左に1が付与される
print('(~3)>>1', (~3)>>1, bin((~3)>>1))
print('(~-3)>>1', (~-3)>>1, bin((~-3)>>1))
print('(~3)<<1', (~3)<<1, bin((~3)<<1))
print('(~-3)<<1', (~-3)<<1, bin((~-3)<<1))
