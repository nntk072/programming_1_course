"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file

An example:
Drive ahead on the X-axis:
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number(
        "How many liters of gas does the car " + "consume per hundred kilometers? "
    )
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print(
            "Coordinates x={:.1f}, y={:.1f}, "
            "the tank contains {:.1f} liters of gas.".format(x, y, gas)
        )

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)
        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)
        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, to_fill, gas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    filled_gas = min(tank_size - gas, to_fill)
    gas += filled_gas
    return gas

def drive(x, y, dest_x, dest_y, gas, gas_consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """

    # It might be useful to make one or two assisting functions
    # to help the implementation of this function.

    distance = calculate_distance(x, y, dest_x, dest_y)
    required_gas = calculate_gas_consumption(distance, gas_consumption)
    if required_gas > gas:
        # change the destination to the point where the car runs out of gas
        dest_x = x + (dest_x - x) * (gas / required_gas)
        dest_y = y + (dest_y - y) * (gas / required_gas)
        required_gas = gas
    gas -= required_gas
    x = dest_x
    y = dest_y
    return gas, x, y

# Implement your own functions here. You are required to
# implement at least two functions that take at least
# one parameter and return at least one value.  The
# functions have to be used somewhere in the program.
def calculate_distance(x1, y1, x2, y2):
    """
    :param x1: float
    :param y1: float
    :param x2: float
    :param y2: float
    :return: float
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_gas_consumption(distance, gas_consumption):
    """
    :param distance: float
    :param gas_consumption: float
    :return: float
    """
    return (gas_consumption / 100) * distance

def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
