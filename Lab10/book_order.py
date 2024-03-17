# Author Jose Tellez
import sys
from book_order_utils import *


def main():
    order_num = input("Enter the order number: ")
    sys.argv.append(order_num)
    title = input("Enter the book title: ")
    sys.argv.append(title)
    author = input("Enter the book author: ")
    sys.argv.append(author)
    isbn = input("Enter the book ISBN: ")
    sys.argv.append(isbn)
    year_pub = input("Enter the year the publication: ")
    sys.argv.append(year_pub)
    quantity = input("Enter the order quantity: ")
    sys.argv.append(quantity)
    cost_cad = input("Enter the order_cost: ")
    sys.argv.append(cost_cad)
    print(len(sys.argv))

    if len(sys.argv) != 8:
        raise ValueError("Number of command line arguments does not match requirement")

    try:
        validate_book_order_details(int(order_num), title, author, int(isbn),
                                    int(year_pub), int(quantity), float(cost_cad))

        unit_cost_cad = calculate_per_book_cost_cad(float(cost_cad), int(quantity))
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
