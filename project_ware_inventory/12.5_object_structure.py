"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
StudentId: 151317891
Name:      Nguyen The Long
Email:     long.nguyen@tuni.fi

StudentId: 151394898
Name:      Vu Dinh Thi
Email:     thi.vu@tuni.fi

Assignment: Using practical tools for fixing, showing the data of the product by code
"""

# +--------------------------------------------------------------+
# | This template file requires at minimum Python version 3.8 to |
# | work correctly. If your Python version is older, you really  |
# | should get yourself a newer version.                         |
# +--------------------------------------------------------------+


LOW_STOCK_LIMIT = 30


class Product:
    """
    This class represent a product i.e. an item available for sale.
    """

    def __init__(self, code, name, category, price, stock):
        self.__code = code
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock

    def __str__(self):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests.
        """

        lines = [
            f"Code:     {self.__code}",
            f"Name:     {self.__name}",
            f"Category: {self.__category}",
            f"Price:    {self.__price:.2f}€",
            f"Stock:    {self.__stock} units",
        ]

        longest_line = len(max(lines, key=len))

        for i in range(len(lines)):
            lines[i] = f"| {lines[i]:{longest_line}} |"

        solid_line = "+" + "-" * (longest_line + 2) + "+"
        lines.insert(0, solid_line)
        lines.append(solid_line)

        return "\n".join(lines)

    def __eq__(self, other):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests since the read_database function will
        stop working correctly.
        """

        return self.__code == other.__code and \
               self.__name == other.__name and \
               self.__category == other.__category and \
               self.__price == other.__price

    def modify_stock_size(self, amount):
        """
        YOU SHOULD NOT MODIFY THIS METHOD since read_database
        relies on its behavior and might stop working as a result.

        Allows the <amount> of items in stock to be modified.
        This is a very simple method: it does not check the
        value of <amount> which could possibly lead to
        a negative amount of items in stock. Caveat emptor.

        :param amount: int, how much to change the amount in stock.
                       Both positive and negative values are accepted:
                       positive value increases the stock and vice versa.
        """

        self.__stock += amount

    def check_stock_size(self):
        """
        Exporting private attribute self.__stock
        :return: integer
        """
        return self.__stock

    def check_price(self):
        """
        Exporting private attribute self.__price
        :return: integer
        """
        return self.__price

    def check_category(self):
        """
        Exporting private attribute self.__price
        :return: integer
        """
        return self.__category

    def change_the_price(self, percentage):
        """
        Change the price of the product based on the category
        :param percentage: The percentage we need to change
        """
        self.__price = self.__price * (100 - percentage) / 100

    def recover_the_price(self, number):
        """
        Changing the original value of the price
        :param number: the original value of the prodcut
        """
        self.__price = number


def _read_lines_until(fd, last_line):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION since read_database
    relies on its behavior and might stop working as a result.

    Reads lines from <fd> until the <last_line> is found.
    Returns a list of all the lines before the <last_line>
    which is not included in the list. Return None if
    file ends bofore <last_line> is found.
    Skips empty lines and comments (i.e. characeter '#'
    and everything after it on a line).

    You don't need to understand this function works as it is
    only used as a helper function for the read_database function.

    :param fd: file, file descriptor the input is read from.
    :param last_line: str, reads lines until <last_line> is found.
    :return: list[str] | None
    """

    lines = []

    while True:
        line = fd.readline()

        if line == "":
            return None

        hashtag_position = line.find("#")
        if hashtag_position != -1:
            line = line[:hashtag_position]

        line = line.strip()

        if line == "":
            continue

        elif line == last_line:
            return lines

        else:
            lines.append(line)


def read_database(filename):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION as it is ready.

    This function reads an input file which must be in the format
    explained in the assignment. Returns a dict containing
    the product code as the key and the corresponding Product
    object as the payload. If an error happens, the return value will be None.

    You don't necessarily need to understand how this function
    works as long as you understand what the return value is.
    You can probably learn something new though, if you examine the
    implementation.

    :param filename: str, name of the file to be read.
    :return: dict[int, Product] | None
    """

    data = {}

    try:
        with open(filename, mode="r", encoding="utf-8") as fd:

            while True:
                lines = _read_lines_until(fd, "BEGIN PRODUCT")
                if lines is None:
                    return data

                lines = _read_lines_until(fd, "END PRODUCT")
                if lines is None:
                    print(f"Error: premature end of file while reading '{filename}'.")
                    return None

                # print(f"TEST: {lines=}")

                collected_product_info = {}

                for line in lines:
                    keyword, value = line.split(maxsplit=1)  # ValueError possible

                    # print(f"TEST: {keyword=} {value=}")

                    if keyword in ("CODE", "STOCK"):
                        value = int(value)  # ValueError possible

                    elif keyword in ("NAME", "CATEGORY"):
                        pass  # No conversion is required for string values.

                    elif keyword == "PRICE":
                        value = float(value)  # ValueError possible

                    else:
                        print(f"Error: an unknown data identifier '{keyword}'.")
                        return None

                    collected_product_info[keyword] = value

                if len(collected_product_info) < 5:
                    print(f"Error: a product block is missing one or more data lines.")
                    return None

                product_code = collected_product_info["CODE"]
                product_name = collected_product_info["NAME"]
                product_category = collected_product_info["CATEGORY"]
                product_price = collected_product_info["PRICE"]
                product_stock = collected_product_info["STOCK"]

                product = Product(code=product_code,
                                  name=product_name,
                                  category=product_category,
                                  price=product_price,
                                  stock=product_stock)

                # print(product)

                if product_code in data:
                    if product == data[product_code]:
                        data[product_code].modify_stock_size(product_stock)

                    else:
                        print(f"Error: product code '{product_code}' conflicting data.")
                        return None

                else:
                    data[product_code] = product

    except OSError:
        print(f"Error: opening the file '{filename}' failed.")
        return None

    except ValueError:
        print(f"Error: something wrong on line '{line}'.")
        return None


def example_function_for_example_purposes(warehouse, parameters):
    """
    This function is an example of how to deal with the extra
    text user entered on the command line after the actual
    command word.

    :param warehouse: dict[int, Product], dict of all known products.
    :param parameters: str, all the text that the user entered after the command word.
    """

    try:
        # Let's try splitting the <parameters> string into two parts.
        # Raises ValueError if there are more or less than exactly two
        # values (in this case there should be one int and one float) in
        # the <parameters> string.
        code, number = parameters.split()

        # First parameter was supposed to be a products code i.e. an integer
        # and the second should be a float. If either of these assumptions fail
        # ValueError will be raised.
        code = int(code)
        number = float(number)

    except ValueError:
        print(f"Error: bad parameters '{parameters}' for example command.")
        return

    # <code> should be an existing product code in the <warehouse>.
    if code not in warehouse:
        print(f"Error: unknown product code '{code}'.")
        return

    # All the errors were checked above, so everything should be
    # smooth sailing from this point onward. Of course, the other
    # commands might require more or less error/sanity checks, this
    # is just a simple example.

    print("Seems like everything is good.")
    print(f"Parameters are: {code=} and {number=}.")


def is_number(string):
    """
    Check if the string is an integer
    :param string
    :return bool
    """

    editstring = string
    if not string.startswith("-") and not string.startswith("+"):
        editstring = "+" + string
    return (editstring.startswith("-") or editstring.startswith("+")) and editstring[1:].isdigit()


def is_float(string):
    """
    Check if the string is a float
    :param string
    :return boolean
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def print_all_products(dictionary_data):
    """
    Print the whole data into the model box as the same of example
    :param dictionary_data: dict, the data after we can get from filename
    """
    my_dict = dictionary_data.copy()

    # Print the keys and values in the dictionary
    for key in sorted(my_dict):
        print(my_dict[key])


def print_one_product(dictionary_data, parameters):
    """
    Print only data of 1 product based on the "CODE"
    :param parameters: str, all the text that the user entered after the command word.
    :param dictionary_data: dictionary, the data after we can get from filename
    """
    my_dict = dictionary_data.copy()
    parameters_in_list = parameters.split()

    # Checking the length of input and the type of parameters input
    if len(parameters_in_list) != 1 or not is_number(parameters_in_list[0]):
        print(f"Error: product '{parameters}' can not be printed as it does not exist.")
        return

    # Print the product if exist
    for key in sorted(my_dict):
        if int(parameters) == key:
            print(my_dict[key])
            return

    # Print the error that the product specified by the code does not exist.
    print(f"Error: product '{parameters}' can not be printed as it does not exist.")


def delete(dictionary_data, parameters):
    """
    Delete the product base on finding the "CODE"
    :param parameters: str, all the text that the user entered after the command word.
    :param dictionary_data: dict, the data after we can get from filename
    """

    # Check if the product code is existed and the format of parameters is right
    parameters_in_list = parameters.split()
    if len(parameters_in_list) != 1 or not is_number(parameters_in_list[0]):
        # The entered code is not an integer or it is unknown.
        print(f"Error: product '{parameters}' can not be deleted as it does not exist.")
        return

    # Find and delete the product
    for key in sorted(dictionary_data):
        if int(parameters_in_list[0]) == key:
            # Check if the stock of the product > 0
            if dictionary_data[key].check_stock_size() > 0:
                print(f"Error: product '{parameters}' can not be deleted as stock remains.")
                return

            # Delete the product
            del dictionary_data[key]
            return

    # Print the error that the product specified by the code does not exist.
    print(f"Error: product '{parameters}' can not be deleted as it does not exist.")


def change_the_stock(dictionary_data, parameters):
    """
    Change the stock of the product
    :param parameters: str, all the text that the user entered after the command word.
    :param dictionary_data: dict, the data after we can get from filename
    """
    parameters_in_list = parameters.split()

    # Check if the product code is existed and the format of parameters is right
    if len(parameters_in_list) != 2 or not is_number(parameters_in_list[0]) or not is_number(parameters_in_list[1]):
        print(f"Error: bad parameters '{parameters}' for change command.")
        return

    # Change the stock size
    for key in sorted(dictionary_data):
        if int(parameters_in_list[0]) == key:
            dictionary_data[key].modify_stock_size(int(parameters_in_list[1]))
            return

    # Print the error that the product specified by the code does not exist.
    print(f"Error: stock for '{parameters_in_list[0]}' can not be changed as it does not exist.")


def low(dictionary_data):
    """
    Print the product whose stock is less than "LOW_STOCK_LIMIT"
    :param dictionary_data: dict, the data after we can get from filename
    """
    dictionary_data_less_than_stock = {}

    # Find and add the requirement products to a new dictionary
    for key in sorted(dictionary_data):
        if dictionary_data[key].check_stock_size() < LOW_STOCK_LIMIT:
            dictionary_data_less_than_stock.update({key: dictionary_data[key]})

    # Print the requirement products
    print_all_products(dictionary_data_less_than_stock)


def combine(dictionary_data, parameters):
    """
    Delete the product base on finding the "CODE" and comparing the prices, categories to combine the data together
    :param dictionary_data: dict, the data after we can get from filename
    :param parameters: str, all the text that the user entered after the command word.
    """

    # Check the format of parameters
    parameters_in_list = parameters.split()
    if len(parameters_in_list) != 2 or not is_number(parameters_in_list[0]) or not is_number(parameters_in_list[1]):
        print(f"Error: bad parameters '{parameters}' for combine command.")
        return

    # Check the entered codes (a product can't be combined itself).
    if parameters_in_list[0] == parameters_in_list[1]:
        print(f"Error: bad parameters '{parameters}' for combine command.")
        return

    # Find and combine the products
    for key in sorted(dictionary_data):
        # find the first product
        if int(parameters_in_list[0]) == key:
            for anotherkey in sorted(dictionary_data):

                # find the second product
                if int(parameters_in_list[1]) == anotherkey:

                    # check if same category
                    if dictionary_data[key].check_category() == dictionary_data[anotherkey].check_category():

                        # check if same price
                        if dictionary_data[key].check_price() == dictionary_data[anotherkey].check_price():
                            dictionary_data[key].modify_stock_size(dictionary_data[anotherkey].check_stock_size())

                            # delete the second product
                            del dictionary_data[anotherkey]
                            return
                        else:
                            print(f"Error: combining items with different prices {dictionary_data[key].check_price()}"
                                  f"€ and {dictionary_data[anotherkey].check_price()}€.")
                            return
                    else:
                        print(
                            f"Error: combining items of different categories "
                            f"'{dictionary_data[key].check_category()}' and "
                            f"'{dictionary_data[anotherkey].check_category()}'.")
                        return

    # Print the error that the product specified by the code does not exist.
    print(f"Error: bad parameters '{parameters}' for combine command.")


def sale(dictionary_data, parameters, filename):
    """
    Make the price of the product to be on sale if the products are in the same categories
    :param filename: string, name of the file to be read.
    :param dictionary_data: dict, the data after we can get from filename
    :param parameters: str, all the text that the user entered after the command word.
    """

    dictionary_before_sale = read_database(filename)
    parameters_in_list = parameters.split()

    # Check the format of parameters
    if len(parameters_in_list) != 2 or not is_float(parameters_in_list[1]):
        print(f"Error: bad parameters '{parameters}' for sale command.")
        return

    count = 0  # The value of changed items

    # Find and change the price of the products based on the category
    for key in sorted(dictionary_data):
        if dictionary_data[key].check_category() == parameters_in_list[0]:
            # If the percentage value = 0.0, return the beginning value of the product
            if parameters_in_list[1] == "0.0":
                if dictionary_data[key].check_price() != dictionary_before_sale[key].check_price():
                    dictionary_data[key].recover_the_price(dictionary_before_sale[key].check_price())
                    count += 1

            # Else, change the value of the items based on the original value of the products
            else:
                dictionary_data[key].recover_the_price(dictionary_before_sale[key].check_price())
                dictionary_data[key].change_the_price(float(parameters_in_list[1]))
                count += 1

    # Print the number of changed items
    print(f"Sale price set for {count} items.")


def main():
    filename = input("Enter database name: ")
    warehouse = read_database(filename)
    if warehouse is None:
        return
    while True:
        command_line = input("Enter command: ").strip()

        if command_line == "":
            return

        command, *parameters = command_line.split(maxsplit=1)

        command = command.lower()

        if len(parameters) == 0:
            parameters = ""
        else:
            parameters = parameters[0]

        # If you have trouble understanding what the values
        # in the variables <command> and <parameters> are,
        # remove the '#' comment character from the next line.
        # print(f"TEST: {command=} {parameters=}")

        if "example".startswith(command) and parameters != "":
            """
            'Example' is not an actual command in the program. It is
            implemented only to allow you to get ideas how to handle
            the contents of the variable <parameters>.

            Example command expects user to enter two values after the
            command name: an integer and a float:

                Enter command: example 123456 1.23

            In this case the variable <parameters> would refer to
            the value "123456 1.23". In other words, everything that
            was entered after the actual command name as a single string.
            """

            example_function_for_example_purposes(warehouse, parameters)
        elif "print".startswith(command) and parameters == "":
            print_all_products(warehouse)
        elif "print".startswith(command) and parameters != "":
            print_one_product(warehouse, parameters)
        elif "delete".startswith(command) and parameters != "":
            delete(warehouse, parameters)
        elif "change".startswith(command) and parameters != "":
            change_the_stock(warehouse, parameters)
        elif "low".startswith(command) and parameters == "":
            low(warehouse)
        elif "combine".startswith(command) and parameters != "":
            combine(warehouse, parameters)
        elif "sale".startswith(command) and parameters != "":
            sale(warehouse, parameters, filename)
        else:
            print(f"Error: bad command line '{command_line}'.")


if __name__ == "__main__":
    main()
