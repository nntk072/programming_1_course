"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *

NAN = ""


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__a = ""
        self.__result_numbervalue = NAN
        self.__result_textvalue = NAN
        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)
        self.__weightlabel = Label(self.__mainwindow, text="Weight:")
        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)
        self.__heightlabel = Label(self.__mainwindow, text="Height:")
        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="Calculate", background="green",
                                         command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="BMI:")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text=self.__a)
        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Stop", command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weightlabel.grid(row=0, column=0, sticky=E)
        self.__heightlabel.grid(row=0, column=3, sticky=E)
        self.__weight_value.grid(row=0, column=1, columnspan=2)
        self.__height_value.grid(row=0, column=4)
        self.__calculate_button.grid(row=1, column=0)
        self.__stop_button.grid(row=1, column=1)
        self.__result_text.grid(row=2, column=0)
        self.__explanation_text.grid(row=3, column=0)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            a = float(self.__weight_value.get())
            b = float(self.__height_value.get())
            if a > 0 and b > 0:
                self.__result_numbervalue = a / ((b / 100) ** 2)
                self.__result_text.configure(text="BMI:")
                if self.__result_numbervalue < 18.5:
                    self.__result_textvalue = "You are underweight."
                elif 18.5 <= self.__result_numbervalue <= 25:
                    self.__result_textvalue = "Your weight is normal."
                else:
                    self.__result_textvalue = "You are overweight."
                self.__result_text.configure(text=f"{self.__result_numbervalue:.2f}")
                self.__explanation_text.configure(text=self.__result_textvalue)
            else:
                self.__result_numbervalue = ""
                self.__result_text.configure(text=self.__result_numbervalue)
                self.__result_textvalue = "Error: height and weight must be positive."
                self.__explanation_text.configure(text=self.__result_textvalue)

        except:
            self.__result_textvalue = "Error: height and weight must be numbers."
            self.__result_numbervalue = ""
            self.__result_text.configure(text=self.__result_numbervalue)
            self.__explanation_text.configure(text=self.__result_textvalue)
            self.__result_text.configure(text="")

        pass

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        pass

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
