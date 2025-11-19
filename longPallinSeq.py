def longestPalindromeSubsequence(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    # Base case: single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    # Build DP table
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # Reconstruct the palindrome from dp table
    i, j = 0, n - 1
    left = []
    right = []

    while i <= j:
        if s[i] == s[j]:
            if i == j:
                left.append(s[i])  # center character
            else:
                left.append(s[i])
                right.append(s[j])
            i += 1
            j -= 1
        else:
            if dp[i+1][j] >= dp[i][j-1]:
                i += 1
            else:
                j -= 1

    # Construct full palindrome
    palindrome = ''.join(left + right[::-1])

    return dp[0][n-1], palindrome


# ---------- MAIN ----------
s = input("Enter string: ")
length, pal = longestPalindromeSubsequence(s)

print("Length of LPS:", length)
print("Longest Palindromic Subsequence:", pal)
