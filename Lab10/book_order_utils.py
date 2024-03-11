# Author Jose Tellez
import re


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
    try:
        order_num_test = int(order_num)
        title_regex = r"([A-Za-z ]){1,}.*"
        author_regex = r"([A-Za-z ]){1,}.*"
        ISBN_regex = r"^[0-9]{4,20}$"
        year_regex = r"^[0-9]{4}$"
        cost_regex = r"^[0-9]{1,}\.[0-9]{2}$"

        # Check order number
        if order_num_test < 0 or order_num_test > 9999:
            raise ValueError("Order Number is invalid")
        # Check title
        if not re.match(title_regex, title):
            raise ValueError("Title is invalid")
        # Check author
        if not re.match(author_regex, author):
            raise ValueError("Author is invalid")
        # Check ISBN
        if not isinstance(isbn, int):
            raise TypeError("ISBN must be an integer")
        elif not re.match(ISBN_regex,isbn):
            raise ValueError("ISBN is invalid")
        # Check Year of publication
        if not isinstance(year_pub, int):
            raise TypeError("Year must be an integer")
        elif not re.match(year_regex, year_pub):
            raise ValueError("Year is invalid")
        # Check quantity
        if not isinstance(quantity,int):
            raise TypeError("Quantity must be an integer")
        elif quantity < 0 or quantity > 1000:
            raise ValueError("Quantity is invalid")
        # Check price
        if not re.match(cost_regex,str(cost_cad)):
            raise ValueError("Cost is invalid")

    except ValueError:
        print("Input should be numbers")

    finally:
        return None


def calculate_per_book_cost_cad(cost_cad, quantity):
    pass


def write_book_order_details(filename, title, author, isbn, year_pub, quantity, cost_cad, unit_cost_cad):
    pass
