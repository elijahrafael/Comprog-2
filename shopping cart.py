def shopping_cart():
    cart = []

    while True:
        print("\nShopping Cart Menu")
        print("[1] Add Item")
        print("[2] View Cart")
        print("[3] Remove Item")
        print("[4] Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            item = input("Enter item name: ")
            cart.append(item)
            print(item, "added to cart")

        elif choice == "2":
            print("Items in your cart:")
            for i in cart:
                print("-", i)

        elif choice == "3":
            item = input("Enter item to remove: ")
            if item in cart:
                cart.remove(item)
                print(item, "removed from cart")
            else:
                print("Item not found")

        elif choice == "4":
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice")

shopping_cart()