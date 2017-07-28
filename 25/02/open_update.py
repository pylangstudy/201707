import datetime
file_name = 'open_update.txt'
#with open(file_name, '+') as f: #ValueError: Must have exactly one of create/read/write/append mode and at most one plus
with open(file_name, '+a') as f: #ValueError: Must have exactly one of create/read/write/append mode and at most one plus
    f.write('{0:%Y-%m-%d %H:%M:%S.%f}\n'.format(datetime.datetime.now()))
    print(f.read())
