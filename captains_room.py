from collections import Counter

# The first line of input (k) is the size of each group, but isn't
# strictly necessary to find the single unique room.
k = int(input())

# The second line of input is the list of room numbers
room_numbers = list(map(int, input().split()))

# Count the occurrences of each room number
counts = Counter(room_numbers)

# Find the key (room number) whose value (count) is 1
for room_number, count in counts.items():
    if count == 1:
        print(room_number)
        break
    
# Input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2