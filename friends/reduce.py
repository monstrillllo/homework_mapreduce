import sys

current_following = None
current_group_followers = []

for line in sys.stdin:
    following, person = line.strip().split('<-')

    if current_following != following and current_following:
        output = f'{current_following} <-'
        for i in current_group_followers:
            output += i
        print(output)
        current_group_followers = []
        current_group_followers.append(person)
    else:
        current_group_followers.append(person)
        
    current_following = following
if current_following:
    output = f'{current_following} <-'
    for i in current_group_followers:
        output += i
    print(output)

    