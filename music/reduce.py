import sys

current_track = None
share_count = 0 
radion_count = 0
skip_count = 0
not_skipped = 0
counter = 0
for line in sys.stdin:
    try:
        tid, uid, share, radio, skip = line.strip().split(',')
        if current_track != tid and current_track:
            print(f'{current_track}\t{share_count}\t{radion_count}\t{not_skipped}\t{skip_count}')
            share_count = 0
            radion_count = 0
            skip_count = 0
            not_skipped = 0
        else:
            share_count += int(share)
            radion_count += int(radio)
            if int(skip) > 0:
                skip_count += 1
            else:
                not_skipped += 1
        current_track = tid
    except:
        continue
if current_track:
    print(f'{current_track}\t{share_count}\t{radion_count}\t{not_skipped}\t{skip_count}')
