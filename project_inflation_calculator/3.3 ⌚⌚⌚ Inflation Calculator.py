"""You will implement a program which can be used to figure out the maximum inflation increase from the values the
user entered. In other words: which is the largest difference between the consecutive entered values.
"""


def main():
    a = 2
    i = 1
    truoc = 0.0
    sau = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    best3 = -9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    """
    test = input("test: ")
    
    if test:= "":
        print(type(test))
    """
    while a <= 2:
        b = input(f"Enter inflation rate for month {i}: ")
        if b != "":
            if i % 2 == 1:
                truoc = float(b)
            else:
                sau = float(b)
            if i % 2 == 1 and truoc - sau >= best3:
                best3 = (truoc - sau)
            elif i % 2 == 0 and sau - truoc >= best3:
                best3 = (sau - truoc)

        i += 1
        if b == "":  # checking 2 variables or not
            if i <= 3:
                print("Error: at least 2 monthly inflation rates must be entered.")
            else:
                print(f"Maximum inflation rate change was {best3:.1f} points.")
            a += 1


if __name__ == "__main__":
    main()
