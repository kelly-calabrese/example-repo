# This program will read from the text file inventory.txt and perform a series
# of tasks with the data to prepare a presentation.

# Import tabulate to make a table of data
from tabulate import tabulate

# Import OS to locate files
import os
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'inventory.txt')

# ========The beginning of the class==========


class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        for self in shoe_list:
            print(f"{self.product} cost: {self.cost}")

    def get_quantity(self):
        for self in shoe_list:
            print(f"{self.product} quantity: {self.quantity}")

    def __str__(self):
        # Display all attributes of the object as a string for printing
        return f"Shoe: {self.product}\n\
                Country: {self.country}\n\
                Code: {self.code}\n\
                Cost: {self.cost}\n\
                Quantity: {self.quantity}\n\n"


# =============Shoe list===========


shoe_list = []


# ==Functions outside the class==


def read_shoes_data():
    # Strategy for calling the relative file path was sourced from
    # a Bing Copilot answer.
    try:
        with open(file_path, "r") as file:
            # Start reading at index 1 (skip the header row)
            lines = file.readlines()[1:]
            for line in lines:
                line = line.rstrip('\n').split(",")
                new_shoe = Shoe(line[0], line[1], line[2],
                                float(line[3]), int(line[4]))
                shoe_list.append(new_shoe)
    except ImportError:
        print("\nError. Return to menu.\n")
    '''
    This function will open the file inventory.txt
    and read the data from the file, then make a shoes object with this data
    and append this object into the shoes list. One line in this file
    represents data to create one object of shoes. You must use the
    try-except in this function for error handling.
    Remember to skip the first line using your code.
    '''


def capture_shoes(country, code, product, cost, quantity):
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''


def view_all():
    for objects in shoe_list:
        print(objects)
        # Print uses the defined __str__ format
    # Tabulate
    col_header = ["Product", "Country", "Code", "Cost", "Quantity"]
    rows = []
    countries = [self.country for self in shoe_list]
    codes = [self.code for self in shoe_list]
    products = [self.product for self in shoe_list]
    costs = [self.cost for self in shoe_list]
    quantities = [self.quantity for self in shoe_list]
    for i in range(0, len(shoe_list)):
        rows.append([products[i], countries[i], codes[i], costs[i],
                     quantities[i]])
    table = tabulate(rows, headers=col_header, tablefmt="grid")
    print(table)
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''


def re_stock():
    sorted_shoes = sorted(shoe_list, key=lambda object: object.quantity)
    lowest_quantity = sorted_shoes[0]
    print(f"Lowest stock is for {lowest_quantity.product}.\n\
          Current stock: {lowest_quantity.quantity}\n")
    restock_input = input("How many shoes do you want to add "
                          "to restock this shoe?\n"
                          "Provide an integer value: ")
    try:
        int(restock_input)
    except ValueError:
        restock_input = input("Invalid input.\nProvide an integer value for "
                              "increase in stock quantity: ")
    new_quantity = int(lowest_quantity.quantity) + int(restock_input)
    for object in shoe_list:
        # Find the restocked shoe in the original list and replace with the
        # quantity with the new value
        if object == lowest_quantity:
            object.quantity = new_quantity
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


def search_shoe(which_shoe):
    for objects in shoe_list:
        if objects.code == which_shoe:
            print(objects)
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''


def value_per_item():
    for objects in shoe_list:
        item_value = objects.cost*objects.quantity
        setattr(objects, 'value', item_value)
    # Tabulate
    col_header = ["Product", "Country", "Code", "Cost", "Quantity", "Value"]
    rows = []
    countries = [self.country for self in shoe_list]
    codes = [self.code for self in shoe_list]
    products = [self.product for self in shoe_list]
    costs = [self.cost for self in shoe_list]
    quantities = [self.quantity for self in shoe_list]
    values = [self.value for self in shoe_list]
    for i in range(0, len(shoe_list)):
        rows.append([products[i], countries[i], codes[i], costs[i],
                    quantities[i], values[i]])
    table = tabulate(rows, headers=col_header, tablefmt="grid")
    print(table)
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():
    sorted_shoes = sorted(shoe_list, key=lambda object: object.quantity,
                          reverse=True)  # Sort list by quanitities, descending
    highest_quantity = sorted_shoes[0]
    print(f"\nSale on {highest_quantity.product}.\n\
    Current stock: {highest_quantity.quantity}\n")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


def return_to_menu(return_input):
    return_input = return_input.upper()
    while True:
        if return_input == "Y":
            menu_input = input("\nThis is the inventory program menu.\n"
                               "Choose from the following actions:\n"
                               "1) Import inventory.txt file\n"
                               "2) Manually enter shoe data\n"
                               "3) View shoe list\n"
                               "4) Identify restock needs\n"
                               "5) Identify data for a specific shoe\n"
                               "6) Determine highest quantity for sale\n"
                               "7) View value of stocked shoes\n"
                               "8) Clear shoe list\n"
                               "9) Quit\n"
                               "Choice: ")
            break
        elif return_input == "Q":
            menu_input = "Q"
            break
        else:
            return_input = input("Invalid input.\nEnter \"Y\" to return to "
                                 "menu or \"Q\" to quit: ")
            return_input = return_input.upper()
    return menu_input


def write_shoes_data(shoe_list, update_choice):
    file_path = os.path.join(current_dir, 'inventory_updated.txt')
    if update_choice == "Y":
        try:
            with open(file_path, "w") as file:
                for shoes in shoe_list:
                    file.write(f"{shoes}\n")
        except ImportError:
            print("\nError. Return to menu.\n")
    else:
        pass


# ==========Main Menu=============


# Launch menu and collect initial menu choice
menu_choice = return_to_menu("Y")


while True:
    if menu_choice == "1":
        read_shoes_data()

    elif menu_choice == "2":
        add_choice = input("\nAdd shoe?\nEnter \"Y\" to add a shoe to the list"
                           " of shoes or \"N\" to close the list: \n")
        add_choice = add_choice.upper()
        while True:
            if add_choice == "Y":
                country = input("Enter the country that the shoes are from: ")
                country = country.capitalize()
                code = input("Enter the product code for the shoes: ")
                product = input("Enter the name of the shoes: ")
                product = product.capitalize()
                cost = input("Enter the cost of the shoes: ")
                try:
                    cost = float(cost)
                except ValueError:
                    cost = input("Enter a number for the cost of the shoe: ")
                cost = float(cost)
                quantity = input("Enter the quantity of shoes: ")
                try:
                    quantity = int(quantity)
                except ValueError:
                    quantity = input("Enter an integer value for quantity: ")
                quantity = int(quantity)
                capture_shoes(country, code, product, cost, quantity)
                add_choice = input("Enter \"Y\" to add a shoe to the list of"
                                   " shoes or \"N\" to close the list: \n")
                add_choice = add_choice.upper()
            elif add_choice == "N":
                update_choice = input("Would you like to print an updated "
                                      ".txt file? \n Choice (Y/N): ")
                write_shoes_data(shoe_list, update_choice)
                break
            else:
                print("Invalid input.")
                add_choice = input("\nEnter \"Y\" to add a shoe to the list"
                                   " of shoes or \"N\" to close the list: \n")
                add_choice = add_choice.upper()

    elif menu_choice == "3":
        view_all()

    elif menu_choice == "4":
        re_stock()

    elif menu_choice == "5":
        which_shoe = input("Enter a shoe code to view its data.\nCode: ")
        print("Search results: \n")
        search_shoe(which_shoe)

    elif menu_choice == "6":
        highest_qty()

    elif menu_choice == "7":
        value_per_item()

    elif menu_choice == "8":
        shoe_list = []

    elif menu_choice == "Q" or menu_choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid input.")
        return_input = input("Enter \"Y\" to open the inventory menu or \"Q\""
                             " to quit: ")

    print("\nProcess complete.\n")
    menu_choice = return_to_menu("Y")
