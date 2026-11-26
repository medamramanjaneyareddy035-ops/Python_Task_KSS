#3. Shopping Cart System 
'''Scenario: A user adds items to a shopping cart. 
Task: 
● Store items in a list 
● Convert to set to remove duplicates 
● Use loop + condition to calculate total cost 
● Handle invalid input using try-except
'''
# Shopping Cart

# Store items in a list
cart = ["Apple", "Banana", "Apple", "Orange"]

# Remove duplicates using set
unique_items = set(cart)

print("Shopping Cart:", unique_items)

# Item prices
prices = {
    "Apple": 30,
    "Banana": 10,
    "Orange": 20
}

total = 0

# Calculate total cost
for item in unique_items:
    try:
        if item in prices:
            total += prices[item]
        else:
            print("Item not found:", item)

    except Exception as e:
        print("Error:", e)

print("Total Cost:", total)
