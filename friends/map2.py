import sys 
import itertools

for line in sys.stdin:
    following, followers_list = line.strip().split('<-')
    followers_groups = [list(f) for f in list(itertools.combinations(followers_list.strip().split(' '), 2))]
    for gr in followers_groups:
        gr.sort()
        print(f'{gr[0].strip()} {gr[1].strip()} -> {following.strip()}')