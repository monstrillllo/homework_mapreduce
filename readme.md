Task #1. Music
We have an online music website where users listen to various tracks, the data gets collected like shown below. Write a map reduce program to get following stats:
Number of times the track was shared with others
Number of times the track was listened to on the radio
Number of times the track was listened to in total
Number of times the track was skipped on the radio

The data looks like as shown below:
UserId|TrackId|Shared|Radio|Skip
111115|222|0|1|0
111113|225|1|0|0
111117|223|0|1|1
111115|225|1|0|0

All done. To launch go to music folder and type: 

    cat file.csv | python3 map.py | sort | python3 reduce.py

####################################

Task #2. DNA Counting
The exercise is to implement a kmer counter using hadoop. Conceptually this is very similar to the wordcount program, but since there are no spaces in the human genome, you have to count 3-mers overlapping kmers instead of discrete words.
The idea is if the genome is: ACACACAGT

All done. To launch go to dna folder and type:
    
    cat file.input | python3 map.py | python3 map2.py | sort | python3 reduce.py

####################################

Task #3. Find common friends
Instagram has a list of followers (note that followers are not bi-directional thing on Instagram. If I follow you, does not mean you follow me). They also have lots of disk space and they serve hundreds of millions of requests everyday. They've decided to pre-compute calculations when they can to reduce the processing time of requests. One common processing request is the "You and Joe have 230 friends in common" feature. When you visit someone's profile, you see a list of friends that you have in common. This list doesn't change frequently so it'd be wasteful to recalculate it every time you visited the profile (sure you could use a decent caching strategy, but then I wouldn't be able to continue writing about mapreduce for this problem). We're going to use mapreduce so that we can calculate everyone's common friends once a day and store those results. Later on it's just a quick lookup. We've got lots of disk, it's cheap.
Assume the friends are stored as Person->[List of Friends], our friends list is then:

Input:
A -> B C D
B -> C D
C -> A B

Output:
A B -> C D
A C -> B
B C -> 

It is necessary to find common friends between all all pairs of friends.

Almost everything is done except that if there are no common friends then there will be no recording.
To launch go to friends folder and type: 

    cat file.input | python3 map.py | sort | python3 reduce.py | sort | python3 map2.py | sort | python3 reduce2.py