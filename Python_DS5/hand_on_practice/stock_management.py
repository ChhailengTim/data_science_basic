def add_product(stock):
    product_id = input('Enter the product ID:')
    product_name = input('Enter the product name:')
    quantity = int(input('Enter the quantity:'))
    price = float(input('Enter the price:'))
    stock[product_id] = {
        "name": product_name,
        "quantity": quantity,
        "price": price
    }
    print('Product added successfully.')
    return stock


def edit_product(stock):
    product_id = input('Enter the product ID to edit:')
    if product_id in stock:
        new_name = input('Enter the new product name:')
        new_quantity = int(input('Enter the new quantity:'))
        new_price = float(input('Enter the new price:'))
        stock[product_id] = {
            "name": new_name,
            "quantity": new_quantity,
            "price": new_price
        }
        return stock
        print('Product updated successfully.')
    else:
        print('Product not found.')


def display_products(stock):
    if len(stock) == 0:
        print('No products available.')
    else:
        print('Products:')
        for product_id, product in stock.items():
            print(
                f'ID: {product_id}, Name: {product["name"]}, Quantity: {product["quantity"]}, Price: {product["price"]}')
        print('Total products:', len(stock))


def delete_product(stock):
    product_id = input('Enter the product ID to delete:')
    if product_id in stock:
        del stock[product_id]
        return stock
        print('Product deleted successfully.')
    else:
        print('Product not found.')


def exit_program():
    print('Exiting the program.')
    exit()


stock = {}

while True:
    print('Stock Management Menu:')
    print('1. Add a product')
    print('2. Display products')
    print('3. Edit a product')
    print('4. Delete a product')
    print('5. Exit')
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        stock = add_product(stock)

    elif choice == '2':
        display_products(stock)

    elif choice == '3':
        stock = edit_product(stock)

    elif choice == '4':
        delete_product(stock)

    elif choice == '5':
        exit_program()

    else:
        print('Invalid choice. Please enter a number from 1 to 5.')
