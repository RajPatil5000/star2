# Function to solve the 0-1 Knapsack problem using Dynamic Programming
def knapsack(values, weights, capacity):
    n = len(values)  # Number of items
    # Create a 2D DP array where dp[i][j] represents the maximum value for the first i items with a knapsack capacity of j
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # If we take the item i-1, max value is either with or without this item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Else, don't take item i-1
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]  # Return the max value for n items and capacity

# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]    # Values of items
    weights = [10, 20, 30]     # Weights of items
    capacity = 50              # Knapsack capacity
    max_value = knapsack(values, weights, capacity)
    print("Maximum value in Knapsack =", max_value)
