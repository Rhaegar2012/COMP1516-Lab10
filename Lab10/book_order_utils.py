# Author Jose Tellez
import re
import os


def validate_book_order_details(order_num, title, author, isbn, year_pub, quantity, cost_cad):
    """
    Validates order details in with a try catch pattern
    :param order_num: One or more integer values
    :param title: One or more lower or upper case letters or spaces
    :param author: Zero or more lower or upper case letters
    :param isbn: sequence of integer numbers, between 40 and 20 digits
    :param year_pub: Must be integers, 4 digits exactly
    :param quantity: Must be integers, between 0 and 1000 inclusive
    :param cost_cad: Must be a floating point value with exactly 2 decimal places
    :return:
    """
    order_num_regex = r"^[0-9]{1,4}$"
    title_regex = r"^[a-zA-Z\s]+$"
    author_regex = r"^[A-Za-z' ]*$"
    ISBN_regex = r"^[0-9]{4,20}$"
    year_regex = r"^[0-9]{4}$"
    cost_regex = r"^[0-9]{1,}\.[0-9]{2}$"

    # Check order number
    try:
        order_test = int(order_num)
    except ValueError:
        print("Order Number is invalid")
    if not re.match(order_num_regex, str(order_num)):
        raise ValueError("Order Number is invalid")
    if int(order_num) < 0 or int(order_num) > 9999:
        raise ValueError("Order Number is invalid")
    # Check title
    if not re.match(title_regex, title):
        raise ValueError("Title is invalid")
    # Check author
    if not re.match(author_regex, author):
        raise ValueError("Author is invalid")
    # Check ISBN
    try:
        isbn_test = int(isbn)
    except ValueError:
        raise TypeError("ISBN must be an integer")
    if not re.match(ISBN_regex, str(isbn)):
        raise ValueError("ISBN is invalid")

    # Check Year of publication
    try:
        year_test = int(year_pub)
    except ValueError:
        raise TypeError("Year must be an integer")
    if not re.match(year_regex, str(year_pub)):
        raise ValueError("Year is invalid")
    # Check quantity
    try:
        quantity_test = int(quantity)
    except ValueError:
       raise TypeError("Quantity must be an integer")
    if int(quantity) < 0 or int(quantity) > 1000:
        raise ValueError("Quantity is invalid")
    # Check price
    try:
        cost_cad_test = float(cost_cad)
    except ValueError:
        print("Cost is invalid")
    if not re.match(cost_regex, str(cost_cad)):
        raise ValueError("Cost is invalid")


def calculate_per_book_cost_cad(cost_cad, quantity):
    """
    Calculates the price per book , given whole purchase price and quantity
    :param cost_cad: whole cost as float
    :param quantity: purchase quantity as integer
    :return: cost per book in the order as float
    """
    cost_per_book = None
    try:
        cost_per_book = float(cost_cad/quantity)
        return cost_per_book
    except ValueError:
        raise ZeroDivisionError("float division by zero")


def write_book_order_details(filename, title, author, isbn, year_pub, quantity, cost_cad, unit_cost_cad):
    """
    Creates a new file and writes book purchase information to it
    :param filename: filename as string
    :param title: book title as string
    :param author: author title as string
    :param isbn: book ISBN as int
    :param year_pub: publication year as int
    :param quantity: quantity as int
    :param cost_cad:cost as float
    :param unit_cost_cad:book unit cost as float
    :return:None
    """
    if os.path.exists(filename):
        raise ValueError("Order file name already exists!")
    else:
        file = open(filename, "w")
        file.write("BOOK ORDER\n")
        file.write(f"title={title}\n")
        file.write(f"author={author}\n")
        file.write(f"isbn={isbn}\n")
        file.write(f"year_pub={year_pub}\n")
        file.write(f"quantity={quantity}\n")
        file.write(f"cost_cad={cost_cad}\n")
        file.write(f"unit_cost={unit_cost_cad}\n")
        file.close()


