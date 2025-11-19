def solve():
    # Read n (length of array) and m (length of sets) - not strictly used
    # in the loop but required for input reading.
    try:
        n, m = map(int, input().split())
    except EOFError:
        # Handle cases where input reading fails or ends abruptly
        return
    except ValueError:
        # Handle cases where input format is incorrect
        return

    # Read the main array of numbers
    arr = list(map(int, input().split()))

    # Read set A (numbers that increase happiness)
    A = set(map(int, input().split()))

    # Read set B (numbers that decrease happiness)
    B = set(map(int, input().split()))

    # Initialize happiness score
    happiness = 0

    # Iterate through every element in the main array
    for i in arr:
        if i in A:
            # Check for membership in set A (O(1) operation)
            happiness += 1
        elif i in B:
            # Check for membership in set B (O(1) operation)
            happiness -= 1

    # Print the final happiness score
    print(happiness)

# Execute the solve function
solve()