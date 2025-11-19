def rob(nums):
    prev,curr=0,0
    for money in nums:
        prev,curr = curr, max(curr,prev+money)
    return curr

nums = [2,7,9,3,1]
print(rob(nums))