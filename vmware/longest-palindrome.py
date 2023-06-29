
def longest_palindrome(s):
    n = len(s)
    # Create a table to store the results of subproblems
    dp = [[False] * n for _ in range(n)]
    print(dp)

    # All substrings of length 1 are palindromes
    max_length = 1
    start = 0
    for i in range(n):
        dp[i][i] = True
    
    print(dp)

longest_palindrome('babad')