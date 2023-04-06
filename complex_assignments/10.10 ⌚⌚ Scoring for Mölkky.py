"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


# TODO:
# a) Implement the class Player here.
class Player:
    def __init__(self, a):
        self.__x = 0
        self.__a = a
        self.__point = 0
        self.__i = 0
        self.__t1 = 0
        self.__t2 = 0
        self.__u1 = 0
        self.__u2 = 0
        self.__compare = []
        self.__list = []
        self.__listforfinalvariable = []
        self.__lastvariable1 = 0
        self.__lastvariable2 = 0

    def get_name(self):
        return self.__a

    def add_points(self, x):
        self.__x = x
        self.__compare.append(x)
        if self.__point + x > 50:
            print(f"{self.__a} gets penalty points!")
            self.__point = 25
        else:
            self.__point += x

    def warning(self):
        if 40 <= self.__point < 50:
            print(
                f"{self.__a} needs only {50 - self.__point} points. It's better to avoid knocking down the "
                f"pins with "
                f"higher points.")

    def printout(self):
        self.__i += 1
        haha = int(sum(self.__compare)) / len(self.__compare)
        self.__list.append(haha)
        if self.__i >= 2:
            if self.__list[self.__i - 1] > self.__list[self.__i - 2]:
                print(f"Cheers {self.__a}!")

    def hitpercentage1(self):
        self.__u1 += 1
        if self.__u1 % 2 == 0:
            if self.__i == 0:
                self.__t1 = 0
                self.__lastvariable1 = 0
            elif self.__i >= 1:
                self.__t1 += 1
                if self.__compare[self.__i - 1] == 0:
                    self.__t1 -= 1
                elif self.__compare[self.__i - 1] != 0:
                    self.__t1 -= 0
                self.__lastvariable1 = self.__t1 / self.__i * 100
        else:
            if self.__lastvariable1 != 0:
                self.__lastvariable1 = self.__lastvariable1
            else:
                self.__lastvariable1 = 0
        return self.__lastvariable1

    def hitpercentage2(self):
        self.__u2 += 1
        if self.__u2 % 2 == 1:
            if self.__i == 0:
                self.__t2 = 0
                self.__lastvariable2 = 0
            elif self.__i >= 1:
                self.__t2 += 1
                if self.__compare[self.__i - 1] == 0:
                    self.__t2 -= 1
                elif self.__compare[self.__i - 1] != 0:
                    self.__t2 -= 0
                self.__lastvariable2 = self.__t2 / self.__i * 100
        else:
            if self.__lastvariable2 != 0:
                self.__lastvariable2 = self.__lastvariable2
            else:
                self.__lastvariable2 = 0
        return self.__lastvariable2
    """
    def haha(self):
        print(self.__i)
        print(self.__compare)
        print(self.__t1)
        print(self.__t2)
        print(self.__u1)
        print(self.__u2)
    """
    def has_won(self):
        if self.__point < 50:
            return False
        else:
            return True

    def get_points(self):
        return self.__point


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))
        in_turn.add_points(pts)
        in_turn.warning()
        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        in_turn.printout()
        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.hitpercentage1():.1f}")
        # TODO: d)
        print(
            f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.hitpercentage2():.1f}")  #
        # TODO: d)
        print("")
        #in_turn.haha()
        #print()
        throw += 1


if __name__ == "__main__":
    main()
