# To find the minimum number of coins needed to reach a target value using a given array of coin denominations, 
# you can use a dynamic programming approach. 
# Here's an example of a Python function that solves this problem:

def min_coins(coins, target):
    # Create a list to store the minimum number of coins for each target value
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: 0 coins needed to reach target value 0

    # Iterate over each coin denomination
    for coin in coins:
        # Update the minimum number of coins for each target value
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the minimum number of coins needed to reach the target value
    return dp[target] if dp[target] != float('inf') else -1

coins = [1, 2, 5]
target = 10
print(min_coins(coins, target))  # Output: 3 (minimum coins needed: 5 + 5 + 1)
