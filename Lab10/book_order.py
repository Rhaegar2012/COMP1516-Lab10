# Author Jose Tellez
import sys
from book_order_utils import *


def main():
    order_num = input("Enter the order number: ")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    isbn = input("Enter the book ISBN: ")
    year_pub = input("Enter the year of publication: ")
    quantity = input("Enter the order quantity: ")
    cost_cad = input("Enter the order cost: ")

    if len(sys.argv) != 8:
        raise ValueError("Command line arguments do not match requirement")

    try:
        validate_book_order_details(order_num, title, author, isbn, year_pub, quantity, cost_cad)
        unit_cost_cad = calculate_per_book_cost_cad(cost_cad, quantity)
        write_book_order_details("book_details.txt", title, author, isbn,
                                 year_pub, quantity, cost_cad, unit_cost_cad)
    except ValueError:
        ValueError("Value Error: ")
    except TypeError:
        TypeError("Type Error: ")
    except ZeroDivisionError:
        ZeroDivisionError("No books in Order:")

    finally:
        return


if __name__ == "__main__":
    main()
