# Define menu items, stock values, and prices
menu = ['Coffee', 'Tea', 'Sandwich', 'Cake']  # List containing café items
stock = {'Coffee': 100, 'Tea': 50, 'Sandwich': 30, 'Cake': 20}  # Dictionary containing stock values for each item
price = {'Coffee': 2.5, 'Tea': 1.5, 'Sandwich': 5.0, 'Cake': 3.0}  # Dictionary containing prices for each item

# Calculate total stock worth in the café
total_stock_worth = 0  # Initialize the total stock worth variable
for item in menu:  # Iterate through each item in the menu
    item_value = stock[item] * price[item]  # Calculate the value of current item's stock
    total_stock_worth += item_value  # Add the current item's stock value to the total

# Print the total stock worth
print("Total Stock Worth in the Cafe:", total_stock_worth)
