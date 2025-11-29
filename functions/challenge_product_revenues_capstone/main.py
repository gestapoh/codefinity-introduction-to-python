# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenues = []
    for index in range(len(prices)):
        revenues.append(prices[index] * quantities_sold[index]) 

    return revenues

def formatted_output(revenues):
    new_revenue = sorted(revenues)
    for index in range(len(new_revenue)):
        print(f"{new_revenue[index][0]} has total revenue of ${new_revenue[index][1]}.")

    return new_revenue

revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenues))
print(revenue_per_product)
revenue = formatted_output(revenue_per_product)

# Example of expected output line (do not remove):
print(f"{revenue[0]} has total revenue of ${revenue[1]}")