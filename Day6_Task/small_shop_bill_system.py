# Develop a Python program for a small shop to process customer purchases. Store product 
'''names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
and product details using tuples. Create functions to display products, add items to the cart, and 
calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError 
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
name entered by the user does not exist).
'''

# Small Shop Billing System

# Dictionary: Product names and prices
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

# Set: Product categories
categories = {"Stationery", "Education"}

# Tuple: Product details
product_details = (
    ("Pen", 10, "Stationery"),
    ("Notebook", 50, "Stationery"),
    ("Pencil", 5, "Stationery")
)

# List: Shopping cart
cart = []


# Function to display products
def display_products():
    print("\nAvailable Products:")

    for name, price in products.items():
        print(name, ":", price)


# Function to add items to cart
def add_to_cart():
    try:
        name = input("Enter product name: ")

        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            raise ValueError

        cart.append((name, products[name], quantity))

        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")


# Recursive function to calculate total bill
def calculate_total(items):
    if len(items) == 0:
        return 0

    name, price, quantity = items[0]

    if not isinstance(price, (int, float)):
        raise TypeError

    if not isinstance(quantity, int):
        raise TypeError

    return (price * quantity) + calculate_total(items[1:])


# Function to display cart and total bill
def view_bill():
    try:
        print("\nItems in Cart:")

        for name, price, quantity in cart:
            print(name, "x", quantity)

        total = calculate_total(cart)

        print("Total Bill:", total)

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero.")



while True:
    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            view_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid menu number.")
