def apply_discount(price, discount=0.05):
    return price - price * discount

def apply_tax(price, tax=0.07):
    return price + price * tax

def calculate_total(price, discount=0.05, tax=0.07):
    return apply_tax(apply_discount(price, discount), tax)

print("Total cost with default discount and tax: $", calculate_total(120))
print("Total cost with custom discount and tax: $", calculate_total(100, discount=0.1, tax=0.08))
