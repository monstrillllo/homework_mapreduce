import sys 
import itertools

for line in sys.stdin:
    person, follow_list = line.strip().split('->')
    for gr in follow_list.strip().split(' '):
        print(f'{gr} <- {person}')