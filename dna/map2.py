import sys

current3 = ''
next3 = ''
counter = 0
for ch in sys.stdin:
    if len(current3) != 3:
        current3 += ch.rstrip()
    
    if len(current3) >= 2:
        next3 += ch.rstrip()

    if len(current3) == 3:
        print(current3)
        current3 = next3
        next3 = ch.rstrip()
