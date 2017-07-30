for v in range(16): print(v, bin(v), v.to_bytes(1, byteorder='big'), v.to_bytes(1, byteorder='little'))
