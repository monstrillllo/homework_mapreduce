import sys

current_persons_group = None
current_follow_goup = []

for line in sys.stdin:
    persons_group, follow = line.strip().split(' -> ')

    if current_persons_group != persons_group and current_persons_group:
        output = f'{current_persons_group} -> '
        for i in current_follow_goup:
            output += f'{i} '
        print(output)
        current_follow_goup = []
        current_follow_goup.append(follow)
    else:
        current_follow_goup.append(follow)
        
    current_persons_group = persons_group
if current_persons_group:
    output = f'{current_persons_group} -> '
    for i in current_follow_goup:
        output += f'{i} '
    print(output)

    