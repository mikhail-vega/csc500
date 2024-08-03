class ItemToPurchase:
    """
    A class used to present an item to purchase

    Attributes
    ----------
    item_name: str
      Name of item
    item_price: float
      Price of item
    item_quantity: int
      Quantity of item
    item_description: str
      Description of item
    
    Methods
    ----------
    print_item_cost() -> None
      Prints item information
    """
    def __init__(self, item_name: str = None, item_price: float = 0, item_quantity: int = 0, item_description: str = None) -> None:
        """
        Parameters
        ----------
        item_name: str
          Name of item
        item_price: float
          Price of item
        item_quantity: int
          Quantity of item
        item_description: str
          Description of item
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        return
    
    def print_item_cost(self):
        """
        Prints item's information. Has no parameters.
        """
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")
        return
    
class ShoppingCart():
    """
    A class used to represent a shopping cart

    Attributes
    ----------
    cart_items: list
      A list to hold items to purchase (ItemsToPurchase)
    customer_name: str
      Name of customer's shopping cart
    current_date: str
      Current date

    Methods
    ----------
    add_item(item: ItemToPurchase) -> None
      Adds an item to cart_items list
    remove_item(item_name: str) -> None
      Removes item from cart_items list
    modify_item(item: ItemToPurchase) -> None
      Modifies an item's description, price, and/or quantity
    get_num_items_in_cart() -> int:
      Returns quantity of all items in cart
    get_cost_of_cart() -> float
      Determines and returns the total cost of items in cart
    print_total() -> None
      Outputs total of objects in cart; If cart is empty, output message
    print_descriptions() -> None
      Outputs each item's description
    
    """
    
    cart_items = []

    def __init__(self, customer_name: str = None, current_date: str = "January 1, 2020") -> None:
        """
        Parameters
        ----------
        customer_name: str
          The name of the customer
        current_date: str
          Today's date
        """
        self.customer_name = customer_name
        self.current_date = current_date
        return
    
    def add_item(self, item: ItemToPurchase) -> None:
        """
        Adds an item to cart_items list

        Parameters
        ----------
        item: ItemToPurchase
          An ItemToPurchase object        
        """
        if item:
            self.cart_items.append(item)
        return

    def remove_item(self, item_name: str) -> None:
        """
        Removes item from cart_items list. If item name cannot be found, outputs a message.

        Parameters
        ----------
        item_name: str
          Name of the item to be removed. If item name cannot be found, outputs a message.

        """
        for key, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item_name:
                self.cart_items.pop(key)
                return
        print("Item not found in cart. Nothing removed.")
        return
    
    def modify_item(self, item: ItemToPurchase) -> None:
        """
        Modifies an item's description, price, and/or quantity. If item can be found (by name) 
        in cart, checks if parameter has default values for description, price, and quantity. 
        If not, modify item in cart. If item cannot be found (by name) in cart, outputs a message.

        Parameters
        ----------
        item: ItemToPurchase
          An ItemToPurchase object
        """
        for cart_item in self.cart_items:
            if item.item_name == cart_item.item_name:
                if item.item_price:
                    cart_item.item_price = item.item_price
                if item.item_quantity:
                    cart_item.item_quantity = item.item_quantity
                if item.item_description:
                    cart_item.description = item.item_description
                return
        print("Item not found in cart. Nothing modified.")
        return

    def get_num_items_in_cart(self) -> int:
        """
        Returns quantity of all items in cart. Has no parameters.
        """
        total_num = 0
        for cart_item in self.cart_items:
            total_num += cart_item.item_quantity
        
        return total_num
    
    def get_cost_of_cart(self) -> float:
        """
        Determines and returns the total cost of items in cart. Has no parameters.
        """
        total_cost = 0
        for cart_item in self.cart_items:
            total_cost += (cart_item.item_quantity * cart_item.item_price)
        return total_cost
    
    def print_total(self):
        """
        Outputs total of objects in cart. If cart is empty, outputs a message.
        """
        if not self.cart_items:
            print("Shopping cart is empty.")
            print()
            return
        
        total = 0
        items = self.get_num_items_in_cart()

        print(f"{self.customer_name} - {self.current_date}")
        print(f"Number of items: {items}")
        for item in self.cart_items:
            item.print_item_cost()
            total += (item.item_price * item.item_quantity)
        print(f"Total: ${total:.2f}")
        print()
        return
    
    def print_descriptions(self):
        """
        Outputs each item's description.
        """
        print(f"{self.customer_name} - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")
        print()
        return

if __name__ == '__main__':
    
    # customer's name
    while True:
        try:
            name = str(input("Enter customer's name: "))
        except ValueError:
            print("Incorrect input - please input a valid name")
        else:
            break
    
    # date
    while True:
        try:
            todays_date = str(input("Enter today's date: "))
        except ValueError:
            print("Incorrect input - please input a valid date")
        else:
            break
      
    print(f"Customer name: {name}")
    print(f"Today's date: {todays_date}")
    
    shopping_cart = ShoppingCart(name, todays_date)

    while True:
        try:
            print("MENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")
            selection = str(input("Choose an option: "))
            print()
        except ValueError:
            print("Incorrect input - please input a valid response")
        else:
            match selection:
                case "a":
                    print('ADD ITEM TO CART')
                    try:
                        name = str(input("Enter the item name: "))
                    except ValueError:
                        print("Please input a valid string")
                    try:
                        price = float(input("Please input item price (i.e. 2.50): "))
                    except ValueError:
                        print("Please input a valid float")
                    try:
                        quanity = int(input("Please input item quantity: "))
                    except:
                        print("Please enter a valid integer")
                    try:
                        description = str(input("Please input item description: "))
                    except ValueError:
                        print("Please input a valid string")

                    item = ItemToPurchase(name, price, quanity, description)
                    shopping_cart.add_item(item)

                case "r":
                    try:
                        name = str(input("Please input item name: "))
                    except ValueError:
                        print("Please input a valid string")
                    shopping_cart.remove_item(name)
                case "c":
                    print("CHANGE ITEM QUANTITY")
                    try:
                        name = str(input("Enter the item name: "))
                    except ValueError:
                        print("Please input a valid string")
                    try:
                        quanity = int(input("Enter the new quantity: "))
                    except:
                        print("Please enter a valid integer")
                    
                    item_update = ItemToPurchase(item_name=name,item_quantity=quanity)
                    shopping_cart.modify_item(item=item_update)
                case "i":
                    print("OUTPUT ITEM'S DESCRIPTION")
                    shopping_cart.print_descriptions()
                case "o":
                    print("OUTPUT SHOPPING CART")
                    shopping_cart.print_total()
                case "q":
                    break
                case _:
                    print("Please input a valid selction\n")



        

            