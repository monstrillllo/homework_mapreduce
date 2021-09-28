import sys

for line in sys.stdin:
    uid, tid, share, radio, skip = line.split('|')
    print(f'{tid},{uid}, {share}, {radio}, {skip}')
    