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

    
    return dp[0][n-1]


# ---------- MAIN ----------
s = input("Enter string: ")
length = longestPalindromeSubsequence(s)

print("Length of LPS:", length)
