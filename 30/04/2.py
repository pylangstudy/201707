for v in [v.to_bytes(1, byteorder='big') for v in range(16)]:
    print(v, int.from_bytes(v, byteorder='big'))
