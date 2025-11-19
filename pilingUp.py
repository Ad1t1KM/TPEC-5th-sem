T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print("Yes")
        continue

    # Safe input: read until exactly n numbers come
    blocks = []
    while len(blocks) < n:
        blocks.extend(map(int, input().split()))
    # blocks = blocks[:n]     # in case user enters more

    left = 0
    right = n - 1

    last = float('inf')
    possible = True

    while left <= right:
        if blocks[left] >= blocks[right]:
            choice = blocks[left]
            left += 1
        else:
            choice = blocks[right]
            right -= 1

        if choice > last:
            possible = False
            break

        last = choice

    print("Yes" if possible else "No")
