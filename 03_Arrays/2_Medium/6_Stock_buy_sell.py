
# 📈 Best Time to Buy and Sell Stock :

# 🧩 Problem Description :

# You are given an array prices where prices[i] is the price of a given stock on the i-th day.
# You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If no profit is possible, return 0.


# 🔢 Sample Input & Output

# Input:  prices = [7, 1, 5, 3, 6, 4]
# Output: 5

# Explanation:
# Buy on day 2 (price = 1), sell on day 5 (price = 6), profit = 6 - 1 = 5.

# ⚠️ Edge Cases
# Prices are decreasing: [9, 8, 7, 6] → Return 0
# Only one price or empty array: [] or [5] → Return 0
# Prices remain the same every day: [3, 3, 3, 3] → Return 0

# 🚨 Brute Force Approach
# Try every pair of days (i, j) such that i < j.

# Calculate profit for each and return the maximum.


# def max_profit_brute(prices):
#     max_profit = 0
#     n = len(prices)
#     for i in range(n):
#         for j in range(i+1, n):
#             profit = prices[j] - prices[i]
#             if profit > max_profit:
#                 max_profit = profit
#     return max_profit

# ⚙️ Better Approach (Prefix Minimum Array)
# Maintain a prefix array of minimum prices.

# At each day, calculate profit = price[i] - min_so_far[i].


# def max_profit_better(prices):
#     n = len(prices)
#     if n == 0:
#         return 0
#     min_price = prices[0]
#     max_profit = 0
#     for i in range(1, n):
#         min_price = min(min_price, prices[i])
#         profit = prices[i] - min_price
#         max_profit = max(max_profit, profit)
#     return max_profit


# ✅ Optimal Approach (Single Pass with Tracking Minimum)
# Use two variables:

# min_price → track the lowest price so far

# max_profit → track the maximum profit

# ✔️ Python Code : 

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


✅ Test Cases

print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))    # 0
print(max_profit([1, 2, 3, 4, 5]))    # 4
print(max_profit([2]))               # 0
               

# 🧮 Time and Space Complexity Comparison
# Approach	      Time Complexity	Space Complexity	        Notes
# Brute Force	           O(n²)	          O(1)	        Try all pairs (i < j)
# Better (Prefix)	       O(n)	              O(1)	        Keep updating min price
# Optimal	               O(n)	              O(1)          Single pass with two variables

# 📝 Summary
# Always look for monotonic patterns in price-based problems.

# This is a classic example of using prefix tracking for optimization.

# Avoid brute force unless required for intuition building.

