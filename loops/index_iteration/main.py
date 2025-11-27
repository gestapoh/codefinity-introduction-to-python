prices = [29.99, 45.50, 12.75, 38.20]
discount = [10, 20, 15, 5]

for index in range(len(prices)):
    prices[index] = prices[index] - prices[index] * discount[index] / 100
    print(f"Updated price for item {index}: ${prices[index]:.2f}")