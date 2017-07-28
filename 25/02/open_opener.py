import os

somedir = 'somedir'
os.makedirs(os.path.join(somedir), exist_ok=True)
dir_fd = os.open(somedir, os.O_RDONLY)

def opener(path, flags): return os.open(path, flags, dir_fd=dir_fd)
with open('open_opener.txt', 'w', opener=opener) as f: print(somedir + '/open_opener.txt', file=f)

os.close(dir_fd)
