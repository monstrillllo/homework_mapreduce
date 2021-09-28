import sys

current_triple = None
current_triple_count = 0

for triple in sys.stdin:
    triple = triple.strip()
    if current_triple != triple and current_triple:
        print(f'{current_triple}\t{current_triple_count}')
        current_triple_count = 0
    else:
        current_triple_count += 1
    current_triple = triple
print(f'{current_triple}\t{current_triple_count}')
