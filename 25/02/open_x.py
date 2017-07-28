file_name = 'open_x.txt'
try:
    with open(file_name, 'x') as f: # FileExistsError: [Errno 17] File exists: 'open_x.txt'
        f.write(file_name)
except: pass
#    print(f.read()) # io.UnsupportedOperation: not readable
