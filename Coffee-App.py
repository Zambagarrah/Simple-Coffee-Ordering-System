# Define a class to represent a Coffee item
class Coffee:

    # Initialize Coffee with a name and price
    def __init__(self, name, price):
        self.name = name  # Store the name of the coffee (e.g., "Latte")
        self.price = price  # Store the price of the coffee (e.g., 3.5)


# Define a class to represent a customer's order
class Order:

    # Initialize Order with an empty list to hold coffee items
    def __init__(self):
        self.items = []  # This list will contain Coffee objects added to the order

    # Add a Coffee object to the order
    def add_item(self, coffee):
        # Add the given Coffee object to the items list
        self.items.append(coffee)
        # Confirm addition to the user
        print(f"Added {coffee.name} to your order.")

    # Calculate the total price of all coffees in the order
    def total(self):
        # Sum up the price of each Coffee in items
        return sum(item.price for item in self.items)

    # Display a summary of the order to the user
    def show_order(self):
        if not self.items:  # If the order is empty
            print("No Items in Order.")  # Inform the user
            return  # Exit the method
        print("\nYour Order: ")  # Print a header for the order summary
        # Loop through each Coffee in the order, with numbering starting at 1
        for i, item in enumerate(self.items, 1):
            # Print each coffee's name and price
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total()}\n")  # Print the total cost of the order

    # Handle the checkout process
    def checkout(self):
        if not self.items:  # If the order is empty
            print("Your Cart is Empty.")  # Inform the user
            return  # Exit the method
        self.show_order()  # Show the current order summary
        # Ask user to confirm checkout
        confirm = input("Proceed to Checkout? (y/n): ").strip().lower()
        if confirm == 'y':  # If user confirms
            print("Order Confirmed! Thank You.")  # Print confirmation message
            self.items.clear()  # Clear the order (empty the cart)
        else:
            # Inform user that checkout was cancelled
            print("Checkout Failed.")


# Main function to display menu and handle user input
def main():
    # Create a menu of Coffee objects
    menu = [
        Coffee("Expresso", 2.5),     # Coffee option 1
        Coffee("Latte", 3.5),        # Coffee option 2
        Coffee("Cappuccino", 3.0),   # Coffee option 3
        Coffee("Americano", 2.0)     # Coffee option 4
    ]
    order = Order()  # Create a new, empty order for the user

    # Start the user interaction loop
    while True:
        print("\n=========== COFFEE MENU =========== ")
        # List all coffee options with numbers
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        print("5. View Order")      # Option to view current order
        print("6. Checkout")        # Option to checkout and pay
        print("7. Exit")            # Option to exit the program

        choice = input("Choose an option: ")  # Get user's menu choice
        if choice in ['1', '2', '3', '4']:  # If user selects a coffee
            # Add selected coffee to the order
            order.add_item(menu[int(choice) - 1])
        elif choice == '5':  # If user wants to view order
            order.show_order()  # Display current order
        elif choice == '6':  # If user wants to checkout
            order.checkout()  # Start checkout process
        elif choice == '7':  # If user wants to exit
            print("Thanks for Visiting. Goodbye!")  # Print exit message
            break  # Exit the while loop and end the program
        else:
            print("Invalid Choice!!! Try Again.")  # Handle invalid input


# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
# This line checks if the script is being run directly (not imported)
# If so, it calls the main function to start the program
# This allows the script to be used as a standalone application
# If imported, the main function won't run automatically, allowing for reuse in other scripts
# This is a common Python practice to allow code to be both reusable and executable
# The program provides a simple coffee ordering system with a menu, order management, and checkout functionality
# It allows users to select coffee items, view their order, and proceed to checkout
# The code is structured to be easy to understand and modify, making it suitable for educational purposes
# The classes and methods are clearly defined, promoting good programming practices
# The program can be extended with additional features, such as payment processing or user accounts
# Overall, this code serves as a basic framework for a coffee ordering application
# It can be used as a starting point for more complex applications or as a learning exercise in Python programming
# The code is designed to be user-friendly, with clear prompts and feedback for the user
# It demonstrates fundamental programming concepts such as classes, methods, loops, and conditionals
# The program can be run in any Python environment, making it accessible for learners and developers
# The use of comments throughout the code helps explain the purpose of each section and improves readability
# The program is a good example of how to structure a simple application in Python
# It can be easily modified to include more coffee options, additional features, or different pricing models
# The code is efficient and straightforward, making it suitable for beginners to understand basic programming concepts
# The program can be further enhanced with features like saving orders to a file or integrating with a database
# Overall, this code provides a solid foundation for a coffee ordering application in Python