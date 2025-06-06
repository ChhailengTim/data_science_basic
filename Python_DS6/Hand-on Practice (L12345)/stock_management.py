

def add_product(stock):
    product_id = input("Enter product ID: ")
    if product_id in stock:
        print("Product already exists!")
    else:
        name = input("Enter product name: ")
        quantity = eval(input("Enter quantity: "))
        price = eval(input("Enter price: "))
        stock[product_id] = (name, quantity, price)
        print("Product added successfully!")
    return stock

def edit_product(stock):
    product_id = input("Enter product ID to edit: ")
    if product_id in stock:
        name = input("Enter new product name: ")
        quantity = eval(input("Enter new quantity: "))
        price = eval(input("Enter new price: "))
        stock[product_id] = (name, quantity, price)
        print("Product updated successfully!")
    else:
        print("Product not found!")
    return stock

def display_products(stock):
    if stock:
        print("\nProduct List:")
        print("Product ID\tName\tQuantity\tPrice")
        print("-" * 40)
        for product_id, (name, quantity, price) in stock.items():
            print(product_id, "\t", name, "\t", quantity, "\t", price)
    else:
        print("No products in stock!")
    return stock

def remove_product(stock):
    product_id = input("Enter product ID to remove: ")
    if product_id in stock:
        del stock[product_id]
        print("Product removed successfully!")
    else:
        print("Product not found!")
    return stock

stock = {}
while True:
    print("\nStock Management Menu:")
    print("1. Add Product")
    print("2. Edit Product")
    print("3. Display Products")
    print("4. Remove Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        stock = add_product(stock)
    elif choice == '2':
        stock = edit_product(stock)
    elif choice == '3':
        stock = display_products(stock)
    elif choice == '4':
        stock = remove_product(stock)
    elif choice == '5':
        print("Exiting Stock Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
