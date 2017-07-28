import datetime
file_name = 'open_append.txt'
with open(file_name, 'a') as f:
    f.write('{0:%Y-%m-%d %H:%M:%S.%f}\n'.format(datetime.datetime.now()))
#    print(f.read()) # io.UnsupportedOperation: not readable
# 改行を挿入しないと入らない。print文との整合性がないためわかりにくい。
