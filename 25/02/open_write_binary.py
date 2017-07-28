import datetime
file_name = 'open_write_binary.bin'
with open(file_name, 'wb') as f: #ValueError: Must have exactly one of create/read/write/append mode and at most one plus
    f.write(b'abc\n')
#    print(f.read()) #io.UnsupportedOperation: read
