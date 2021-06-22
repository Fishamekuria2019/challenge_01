# Percent Increase Activity

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create float variable for original_price
original_price = 1922154158.872126315

# Create float variable for current_price
current_price = 2522154154.324545465

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent increase
percent_increase = (increase / original_price) * 100

# Print original_price
print("Apple's original stock price was $" + str(original_price))
print(f"Apple's original stock price was ${original_price:,.2f}.")

# Print current_price
print(f"Apple's current stock price is ${current_price:,.2f}.")

# Print percent increase
print(f"Apple's stock price increased by {percent_increase:.2f}%.")
