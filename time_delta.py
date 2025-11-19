from datetime import datetime

# Function to calculate the time difference in seconds
def time_delta(t1, t2):
    # The required format string based on the HackerRank problem description:
    # Example: Sat 02 May 2015 19:54:36 +0530
    # %a: Weekday as locale’s abbreviated name (Sat)
    # %d: Day of the month as a zero-padded decimal number (02)
    # %b: Month as locale’s abbreviated name (May)
    # %Y: Year with century (2015)
    # %H: Hour (24-hour clock) as a zero-padded decimal number (19)
    # %M: Minute as a zero-padded decimal number (54)
    # %S: Second as a zero-padded decimal number (36)
    # %z: UTC offset in the form +HHMM or -HHMM (+0530)
    fmt = "%a %d %b %Y %H:%M:%S %z"
    
    # Convert string dates to datetime objects
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    
    # Calculate the absolute difference between the two datetime objects.
    # The result is a timedelta object.
    time_difference = abs(dt1 - dt2)
    
    # Convert the timedelta object to the total number of seconds (as a float)
    total_seconds = time_difference.total_seconds()
    
    # Return the total seconds as a string (HackerRank expects string output)
    return str(int(total_seconds))

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input())

    # Loop through all test cases
    for t_itr in range(t):
        # Read the two time strings for the current test case
        time1 = input()
        time2 = input()
        
        # Calculate the delta and print the result
        delta = time_delta(time1, time2)
        print(delta)
        
        
        
# Input
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000