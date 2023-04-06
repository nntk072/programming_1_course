"""
Nguyen The Long long.nguyen@tuni.fi 151317891
Vu Dinh Thi     thi.vu@tuni.fi      151394898
Find maximum, minimum, median, mean, deviation of the input numbers
"""
from math import sqrt


def readinput():
    """Find Median to export the value to the output
    :parameter: None
    :return: list

    """
    a = []
    checkcondition = -1
    while checkcondition < 0:  # use variable to check that I need to input or not
        inputvalue = input()
        if inputvalue == "":  # input = enter means inputvalue is ""
            checkcondition = 1  # end the while loop
        else:
            a.append(float(inputvalue))  # append the value to ethe list
    return a


def Median(a):
    """Find Median to export the value to the output
    :parameter: list
    :return: float
    """
    asorted = sorted(a)  # sort the list to an increasing order
    i = (len(a) - 1) // 2  # find the middle variable of the sorted list

    if len(a) % 2:
        median = asorted[i]  # if the number of variables is even => median = middle variable
    else:
        median = (asorted[i] + asorted[i + 1]) / 2.0  # applying the function to find the median value in Math
    return median


def Mean(a):
    """Find Mean to export the value to the output
    :parameter: list
    :return: float
    """
    mean = float(sum(a)) / len(a)  # applying the function to find the mean value in Math
    return mean


def Deviation(a):
    """Find Deviation to export the value to the output
    :parameter: list
    :return: float
    """
    k = float(sum(a) / float(len(a)))  # applying the function to find intermediate x
    u = 0
    for i in a:
        t = (i - k) * (i - k)  # applying the function to get sigma (xi-x)^2
        u += t  # sum each (xi-x)^2 value
    SD = 1 / (len(a) - 1) * u  # applying the function 1/(N-1)*sigma(xi-x)^2, len(a) = N, sigma(xi-x)^2= u
    standarddeviation = sqrt(SD)  # square root the variance
    return standarddeviation


def main():
    print("Enter seawater levels in centimeters one per line.\nEnd by entering an empty line.")
    a = readinput()
    if len(a) <= 2:  # check if two measurements or not
        print("Error: At least two measurements must be entered!")
    else:
        minvalue = min(a)
        maxvalue = max(a)
        medianvalue = Median(a)
        meanvalue = Mean(a)
        deviationvalue = Deviation(a)
        print(f"Minimum: {minvalue:8.2f} cm")
        print(f"Maximum: {maxvalue:8.2f} cm")
        print(f"Median: {medianvalue:9.2f} cm")
        print(f"Mean: {meanvalue:11.2f} cm")
        print(f"Deviation: {deviationvalue:6.2f} cm")


if __name__ == "__main__":
    main()
