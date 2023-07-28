"""
COMP.CS.100 Programming 1
Fraction calculator
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator):.0f}/{abs(self.__denominator):.0f}"

    def simplify(self):
        """
        Simplify the fraction by dividing both the numerator and the denominator
        by their greatest common divisor.
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator / gcd
        self.__denominator = self.__denominator / gcd


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def multiply(frac1, frac2):
    """
    Multiplies two fractions.

    :param frac1: Fraction, first factor
    :param frac2: Fraction, second factor
    :return: Fraction, the product
    """

    # The product of two fractions is a fraction where the numerator
    # is the product of the two numerators and the denominator is the
    # product of the two denominators.
    numerator = frac1._Fraction__numerator * frac2._Fraction__numerator
    denominator = frac1._Fraction__denominator * frac2._Fraction__denominator
    print(
        f"{frac1.return_string()} * {frac2.return_string()} = {numerator}/{denominator}"
    )
    # Print the simplified fraction
    frac = Fraction(numerator, denominator)
    frac.simplify()
    print(f"simplified {frac.return_string()}")


def main():
    dict = {}
    while True:
        command = input("> ")
        if command == "quit":
            print("Bye bye!")
            break
        elif command == "add":
            frac = input("Enter a fraction in the form integer/integer: ")
            frac = frac.split("/")
            frac1 = Fraction(int(frac[0]), int(frac[1]))
            name = input("Enter a name: ")
            # Save the fraction to the dict with the name as a key
            if name not in dict:
                dict[name] = frac1
        elif command == "print":
            name = input("Enter a name: ")
            if name in dict:
                print(f"{name} = {dict[name].return_string()}")
            else:
                print(f"Name {name} was not found")
        elif command == "list":
            # prints an alphabetical list of the contents of each of the calculator's memory locations. The command prints nothing if no fractions have been saved.
            for key in sorted(dict):
                print(f"{key} = {dict[key].return_string()}")
        elif command == "*":
            name1 = input("1st operand: ")
            if name1 not in dict:
                print(f"Name {name1} was not found")
                continue
            name2 = input("2nd operand: ")
            if name2 not in dict:
                print(f"Name {name2} was not found")
                continue
            multiply(dict[name1], dict[name2])
        elif command == "file":
            filename = input("Enter the name of the file: ")
            try:
                with open(filename, "r") as f:
                    for line in f:
                        line = line.rstrip()
                        line = line.split("=")
                        frac = line[1].split("/")
                        # check if the fraction is valid
                        if len(frac) != 2:
                            print("Error: the file cannot be read.")
                            break
                        # check if the numerator and denominator are integers
                        if frac[0].isdigit() and frac[1].isdigit():
                            frac1 = Fraction(int(frac[0]), int(frac[1]))
                            name = line[0]
                            # Save the fraction to the dict with the name as a key
                            if name not in dict:
                                dict[name] = frac1
            except FileNotFoundError:
                print("Error: the file cannot be read.")

        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
