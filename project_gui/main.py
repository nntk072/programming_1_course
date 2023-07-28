"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

StudentId: 151394898
Name:      Vu Dinh Thi
Email:     thi.vu@tuni.fi

StudentId: 151317891
Name:      Nguyen The Long
Email:     long.nguyen@tuni.fi


Project 13.10: Graphical User Interface

We choose to implement an advanced GUI.

This program is designated to perform a GUI game called Wordle. The game
will choose a random word in a dictionary for the player to guess. The player
can choose whether to play with 4 letters, 5 letters or 6 letters words.

The main menu of the game has 4 options: New Game, Instruction, Leaderboard
and Quit.

The New Game option leads the player into the game.
Before playing, the player has to type in a username for record saving purpose.
If not then the record will be saved as "Anonymous". In each game, the player
have 6 attempts to guess. In each attempt, the player must deliver a proper
word in English, each letter of the word must be typed in separate square
boxes in a row. Through the attempts, the game will give some hints about the
word that need to be guessed based on the player's answer. If the letter is
correct (i.e. exists in the word) but it's not in the right position, then the
background will be marked with orange. If the letter is correct and the
position is also correct, then the background will be marked with green. Note
that 1 letter could appear multiple times, and the game will not give any
hints about this.

The Instruction option leads the player to a window where rules of the games
are shown.

The Leaderboard option shows the top 10 entries of the game.

The Quit option close the game.

The program includes class object with the methods:
@Method main_menu: creates the main menu of the game, which includes the
attribute buttons for the user to choose: start a new game, read the
instructions, view the leaderboard, or quit the game.
@Method instructions_window: creates the instructions window, which shows the
rules of the game to the player.
@Method enter_user_name: creates the window for the user to enter their user
name for record purpose.
@Method store_user_name: stores the user name inputted by the user from the
input_user_name entry containing the player's chosen user name by typing in.
@Method pre_game_frame: creates the window for the user to choose the number
of letters they want to play.
@Method return_to_main_menu: returns the user to the main menu from a
specific frame.
@Method confirmation_return: creates the pop-up window for the user to
confirm if they want to quit the current game and return to the main menu.
@Method main_game_frame: creates the window for the user to play the game.
@Method create_input_boxes: creates input boxes for users to type in letters
for the game.
@Method submit_answer: checks the answer submitted by the user.
@Method check_the_guessed_words_with_the_rules: checks
whether the word the player types in satisfies with all the rules
@Method check_number_of_attempts_used: Checks the number of
attempts used by the user and updates the announcement label accordingly.
@Method check_if_the_word_is_correct: checks if the user's guess is correct
and updates the appearance of the input boxes accordingly (green for correct
letter and position, orange for correct letter but wrong position).
@Method update_time: updates the time taken by the user to
guess the word.
@Method leaderboard_window_display: creates the
leaderboard window, which includes the top 10 entries of the leaderboard. The
result is considered using the attempts used and time taken.
@Method display_entries: shows the top 10 entries with the best results
in the Leaderboard section.
@staticmethod get_leaderboard_entries: gets the users' records in the
file, stores it in a variable and returns a list of leaderboard entries.
@staticmethod add_to_leaderboard: adds the user's score
and other information to the leaderboard file.

"""

from tkinter import *
import random
import time


class GUI:
    def __init__(self):
        # Creating the main window
        self.__main_window = Tk()
        # Set the title for the window
        self.__main_window.title("Wordle!")
        # Set the geometry size for the window
        self.__main_window.geometry("1200x1000")

        # Creating the components of the GUI
        # Set up the title of the game
        self.__game_label = Label(
            self.__main_window, text="WORDLE", font=("Helvetica", 80)
        )
        # Set up the geometry of the title in the window
        self.__game_label.pack()

        # Initialize the frames would be used in the game
        self.__main_menu_frame = None
        self.__enter_user_name_frame = None
        self.__confirmation_return_window = None
        self.__instructions_frame = None
        self.__pre_game_frame = None
        self.__main_game_frame = None
        self.__entry_frame = None

        # Initialize the tools and elements for the main game
        self.__announcement_label = None
        self.__words_dictionary = None
        self.__word_to_guess = None
        self.__list_of_entries = None
        self.__time_label = None
        self.__leaderboard_frame = None
        self.__submit_button = None
        self.__attempt_no = None

        # Initialize the time elements for the main game
        self.__start_time = None
        self.__end_time = None  # Initialize end time
        self.__user_name = None  # Initialize user name

        # Set up the main menu components
        self.main_menu()

        self.__main_window.mainloop()

    def main_menu(self):
        """
        This method creates the main menu of the game, which includes the
        buttons for the user to choose to start a new game, read the
        instructions, view the leaderboard, or quit the game.
        """
        # Creating the menu frame (initial frame)
        self.__main_menu_frame = Frame(self.__main_window)

        # Creating the buttons
        # Creating the New Game button that leads to the New Game Window while
        # clicked
        new_game_button = Button(
            self.__main_menu_frame,
            text="New Game",
            height=3,
            width=10,
            command=self.enter_user_name,
        )

        # Creating the Instructions button that shows the instructions to
        # play the game while clicked
        instructions_button = Button(
            self.__main_menu_frame,
            text="Instructions",
            height=3,
            width=10,
            command=self.instructions_window,
        )

        # Creating the Leaderboard button that shows the Top 10 results from
        # players while clicked
        leaderboard_button = Button(
            self.__main_menu_frame,
            text="Leaderboard",
            height=3,
            width=10,
            command=self.leaderboard_window_display,
        )

        # Creating the Quit button to quit the game
        quit_button = Button(
            self.__main_menu_frame,
            text="Quit",
            height=3,
            width=10,
            command=lambda: self.__main_window.destroy()
        )

        # Set up the geometry of the buttons
        new_game_button.pack()
        instructions_button.pack()
        leaderboard_button.pack()
        quit_button.pack()

        self.__main_menu_frame.pack()

    def instructions_window(self):
        """
        This method creates the instructions window, which includes the rules
        of the game.
        """
        # Destroy the main menu frame
        self.__main_menu_frame.destroy()

        # Create the instructions frame
        self.__instructions_frame = Frame(self.__main_window)

        # Create the instructions label
        instructions_label = Label(
            self.__instructions_frame, text="Instructions",
            font=("Helvetica", 24)
        )

        # Set up the geometry of the instructions label
        instructions_label.pack()

        # Create the rules label, which write out the rules for the game
        rules_label = Label(
            self.__instructions_frame,
            text="This Wordle game requires you to guess a word, "
                 "either 4, 5, or 6 letters, depending on your choice\n\n"
                 "For each word, you will have 6 attempts to guess "
                 "the word.\n\n"
                 "For each attempt, you will have to write the "
                 "guessing word in a line, each box containing one letter.\n\n"
                 "The word must be available in English, and each "
                 "box must be filled with exactly 1 letter, not multiple "
                 "letters, numbers or other symbols.\n\n"
                 "The game will inform the warnings if these rules are not "
                 "satisfied.\n\n"
                 "After each attempt, the game will inform about the word "
                 "you have guessed. Hints are given after each attempt. \n\n"
                 "If the letter appears within an orange square, then the "
                 "letter does appear in the word, but it's not in the right "
                 "position.\n\n"
                 "If the letter appears within a green square, then the letter"
                 " does appear in the word, and it's in the right position. "
                 "\n\n",
            font=("Helvetica", 14),
            # Align the text to the left of the label
            justify=LEFT
        )
        # Set up the geometry for the rules label
        rules_label.pack()

        # Create the return button to return to the main page while clicked
        return_button = Button(
            self.__instructions_frame,
            text="Return to\nmain menu",
            height=3,
            width=10,
            command=lambda: self.return_to_main_menu("instructions"),
        )
        # Set up the geometry of the return button
        return_button.pack(side=BOTTOM)

        self.__instructions_frame.pack()

    def enter_user_name(self):
        """
        This method creates the window for the user to enter their user name.
        """
        # Destroy the main menu frame in order for
        # the new frame to be replaced
        self.__main_menu_frame.destroy()

        # Create the enter_user_name frame
        self.__enter_user_name_frame = Frame(self.__main_window)

        # Create the announcement label
        announcement_label = Label(
            self.__enter_user_name_frame,
            text="Input your user name here",
            height=3,
            width=20,
        )
        # Set up the geometry of the announcement label
        announcement_label.pack()

        # Create the input box for the user name
        input_user_name = Entry(
            self.__enter_user_name_frame,
            width=20,
            justify=CENTER,
            font=("Times", 20, "bold"),
        )

        # Set the geometry for the entry box
        input_user_name.pack()

        # Create the submit button
        submit_button = Button(
            self.__enter_user_name_frame,
            text="Submit",
            height=3,
            command=lambda: self.store_user_name(input_user_name),
        )
        submit_button.pack()
        self.__enter_user_name_frame.pack()

    def store_user_name(self, input_user_name):
        """
        This method stores the user name inputted by the user.
        :param input_user_name: entry, the box containing the player's
        chosen user name by typing in.
        """
        self.__user_name = input_user_name.get()
        self.pre_game_frame()

    def pre_game_frame(self):
        """
        This method creates the window for the user to choose the number of
        letters they want to play.
        """

        # Destroy the enter_user_name frame to replace another frame in
        self.__enter_user_name_frame.destroy()

        # Create the new game window, which includes the buttons for the user
        # choose the number of letters they want to play (4, 5, or 6 letters)
        self.__pre_game_frame = Frame(self.__main_window)

        # Create the game label
        game_label = Label(
            self.__pre_game_frame,
            text="Choose the number of letters" "\nyou want to play",
            font=("Helvetica", 24),
        )
        # Set the geometry for the game label
        game_label.pack()

        # Create the buttons for the player to choose how many letter they
        # want to play
        # The button for 4 letters word
        four_letters_button = Button(
            self.__pre_game_frame,
            text="4 letters",
            height=3,
            width=10,
            command=lambda: self.main_game_frame(4),
        )

        # The button for 5 letters word
        five_letters_button = Button(
            self.__pre_game_frame,
            text="5 letters",
            height=3,
            width=10,
            command=lambda: self.main_game_frame(5),
        )

        # The button for 6 letters word
        six_letters_button = Button(
            self.__pre_game_frame,
            text="6 letters",
            height=3,
            width=10,
            command=lambda: self.main_game_frame(6),
        )

        # Set up the geometry for those above buttons
        # in the New Game window frame
        four_letters_button.pack()
        five_letters_button.pack()
        six_letters_button.pack()

        # Create the return button which returns the player to the main menu
        return_button = Button(
            self.__pre_game_frame,
            text="Return to\nmain menu",
            height=3,
            width=10,
            command=lambda: self.return_to_main_menu("pre_game_frame"),
        )

        # Set the geometry for the return button
        return_button.pack()

        self.__pre_game_frame.pack()

    def return_to_main_menu(self, frame):
        """
        This method returns the user to the main menu.
        :param  frame: str, given the frame name that shall be destroyed
        i.e. the frame where the user is staying at.
        """

        # Reset end time
        self.__end_time = None

        # Destroy the current frame
        if frame == "main_game_window":
            self.__confirmation_return_window.destroy()
            self.__main_game_frame.destroy()
        elif frame == "pre_game_frame":
            self.__pre_game_frame.destroy()
        elif frame == "leaderboard":
            self.__leaderboard_frame.destroy()
        elif frame == "instructions":
            self.__instructions_frame.destroy()

        # Update the window to the main menu
        self.__main_window.update()
        self.main_menu()

    def confirmation_return(self):
        """
        This method creates the window for the user to confirm if they want
        to quit the current game and return to the main menu.
        """

        # Create a window that pops out
        self.__confirmation_return_window = Toplevel()

        # Set the geometry for the pop-out window
        self.__confirmation_return_window.geometry("500x200")

        # Create a label to give the confirmation question to the player
        confirmation_window_label = Label(
            self.__confirmation_return_window,
            text="Do you want to quit " "this game\n"
                 "and return to" " the main menu?",
            font=("Helvetica", 24),
        )

        # Set the geometry for the label in the pop-out window
        confirmation_window_label.pack()

        # Create the yes and no buttons
        yes_button = Button(
            self.__confirmation_return_window,
            text="Yes",
            height=3,
            width=10,
            # If the player choose yes i.e. quit the game, the programme
            # will destroy both the pop-out window and the current frame,
            # and start running the main menu frame
            command=lambda: self.return_to_main_menu("main_game_window"),
        )
        no_button = Button(
            self.__confirmation_return_window,
            text="No",
            height=3,
            width=10,
            # If the player choose no i.e. still continue playing,
            # only the pop-out window is destroyed.
            command=lambda: self.__confirmation_return_window.destroy(),
        )

        # Set the geometry of those buttons
        yes_button.pack()
        no_button.pack()

    def main_game_frame(self, num):
        """
        This method creates the window for the user to play the game.

        :param num: int, the number of letters the user wants to play
        """

        # Destroy the previous frame to replace the main game frame
        self.__pre_game_frame.destroy()

        # Create the main game frame
        self.__main_game_frame = Frame(self.__main_window)

        # Set the title for the frame
        title = "Wordle! " + str(num) + " letters game"

        # Title label
        title_label = Label(
            self.__main_game_frame, text=title, font=("Helvetica", 24)
        )

        # Set the geometry for the title label
        title_label.pack()

        # Announcement label, useful for announcing the attempts as well as
        # warnings to the player.
        self.__announcement_label = Label(
            self.__main_game_frame,
            text="Let's start the game!",
            height=6,
            width=30
        )

        # Set the geometry for the announcement label
        self.__announcement_label.pack()

        # Open the selected dictionary text file based on the number of letters
        file_name = str("dictionary_" + str(num) + "_letters.txt")

        # Save the dictionary words to a list
        self.__words_dictionary = [
            line.strip() for line in
            open(file_name, mode="r", encoding="utf-8")
        ]

        # Randomly choose a word in the dictionary for the player to guess
        self.__word_to_guess = random.choice(self.__words_dictionary)

        self.__attempt_no = 0

        # Creates input boxes for users to type in letters for the game.
        self.create_input_boxes(num)

        # Create the submit button
        self.__submit_button = Button(
            self.__main_game_frame,
            text="Submit",
            height=3,
            command=lambda: self.submit_answer(self.__attempt_no),
        )
        self.__submit_button.pack(side=LEFT)

        # Create the return button
        return_button = Button(
            self.__main_game_frame,
            text="Return",
            height=3,
            command=self.confirmation_return,
        )

        # Set up the geometry for the return button
        return_button.pack(side=LEFT)

        # Timing features
        self.__start_time = time.time()

        # Set up the time label to inform the player the time while playing
        self.__time_label = Label(
            self.__main_game_frame,
            text="Time: 0.00 seconds",
            font=("Helvetica", 16)
        )

        # Set the geometry for the time label
        self.__time_label.pack()

        self.__main_game_frame.pack()

        # Update the time in the label
        self.update_time()

    def create_input_boxes(self, num):
        """
        The method creates input boxes for users to type in letters for the
        game.

        :param num: int, the number of letters the user wants to play
        """
        # Create the frame for the input boxes
        self.__entry_frame = Frame(self.__main_game_frame)
        self.__list_of_entries = []

        # Set the geometry for the entry frame
        self.__entry_frame.pack()

        # Create the input boxes and stores it in a list
        for k in range(0, 6):
            # Each row represents one attempt
            entries_in_a_row = []
            # The number of entries in a row depends on the number of letters
            for i in range(0, num):
                input_box = Entry(
                    self.__entry_frame,
                    width=5,
                    justify=CENTER,
                    font=("Times", 20, "bold"),
                )
                # Set the geometry of the entries
                input_box.grid(row=k, column=i, sticky="nsew")

                # Set all the other rows except for the first row to be
                # disabled so that the player won't be confused on where to
                # type in for the first attempt.
                if k > 0:
                    input_box.config(state="disabled")
                # Add all elements into a row
                entries_in_a_row.append(input_box)
            # Add 6 rows represents 6 attempts to the list
            self.__list_of_entries.append(entries_in_a_row)

    def submit_answer(self, attempt_no):
        """
        This method checks the answer submitted by the user.

        :param attempt_no: the row number in the entries list
            represents the current attempt
        """

        # Check if the type in satisfies with the rules. If yes then continue
        # checking the word. If not then return to inform the player.
        if not self.check_the_guessed_words_with_the_rules(attempt_no):
            return

        # Check if the word the player types in is correct. If yes then stop
        # game and return. If not then continues the game and give hints.
        if self.check_if_the_word_is_correct(attempt_no):
            return

        # Check if the user has used up all the attempts. If yes then return
        # to the game and disabled the game. If not then continues with the
        # attempts
        if self.check_number_of_attempts_used(attempt_no):
            return

        # Add up to mark the current attempt
        self.__attempt_no += 1

        # Enable the entry row corresponding to the next attempt
        for i in range(len(self.__list_of_entries[attempt_no + 1])):
            self.__list_of_entries[attempt_no + 1][i].configure(state="normal")

    def check_the_guessed_words_with_the_rules(self, attempt_no):
        """
        This method checks whether the word the player types in
        satisfies with all the rules

        :param attempt_no: int, the row number in the entries list
            represents the current attempt
        :return: True if the guessing word satisfies all the rules,
                 False otherwise
        """
        # Initialize an empty string to store the guessed letters
        letter_guessed = ""

        # Check if the user has filled all the boxes of the rules
        for i in range(len(self.__list_of_entries[attempt_no])):
            character = self.__list_of_entries[attempt_no][i].get()
            # Check if each box have only 1 character
            if len(character) > 1:
                self.__announcement_label.config(
                    text="Error, each box must " "contain\n1 character only!"
                )
                return False
            # Check if all entries are filled
            elif len(character) != 1:
                self.__announcement_label.config(
                    text="Error, all letter boxes must be filled!"
                )
                return False
            # Check if the index in the box are letters. Either lower or upper
            # letters are allowed.
            elif not (97 <= ord(character.lower()) <= 122):
                self.__announcement_label.config(
                    text="Error, only letters are allowed!"
                )
                return False
            letter_guessed += character.lower()

        # Check if the whole word is available in English
        if letter_guessed not in self.__words_dictionary:
            self.__announcement_label.config(
                text="Error, the word you guessed \n "
                     "is not available in English!"
            )
            return False

        # If all checks pass, return True to indicate a valid guess
        return True

    def check_number_of_attempts_used(self, attempt_no):
        """
        Checks the number of attempts used by the user and updates the
        announcement label accordingly.

        :param attempt_no: int, the row number in the entries list
            represents the current attempt
        :return: True if no more attempts are allowed i.e. all 6 attempts
            have been used, False otherwise
        """
        # Check if the number of attempts is 4 (fifth attempt)
        if self.__attempt_no == 4:
            # Announce last attempt to the user
            self.__announcement_label.config(
                text="Attempt 5 finished!\nLast try!")
            return False

        # Check if the number of attempts is 5 (sixth attempt)
        elif self.__attempt_no == 5:
            self.__announcement_label.config(
                text="Attempt 6 finished!\nGame over!\nThe correct letter is "
                     + self.__word_to_guess
            )
            # Disable the submit button since the game is over
            self.__submit_button.config(state="disabled")
            self.__end_time = time.time()  # Stop the timer
            return True

        # If the number of attempts is less than 5
        # (attempt_no ranges from 0 to 3).
        else:
            self.__announcement_label.config(
                text="Attempt " + str(attempt_no + 1) + " finished!"
            )
            return False

    def check_if_the_word_is_correct(self, attempt_no):
        """
        Checks if the user's guess is correct and updates the appearance of the
        input boxes accordingly (green for correct letter and position,
        orange for correct letter but wrong position).

        :param attempt_no: int, the row number in the entries list
         represents the current attempt
        :return: True if the word guessed is correct, False otherwise
        """

        # Initialize the variable to store the correct letters in the right
        # position for later use
        correct_letters = 0

        # Check if the user has guessed the right word
        # Running through each letter in the word
        for i in range(len(self.__list_of_entries[attempt_no])):
            for k in range(len(self.__list_of_entries[attempt_no])):
                character = self.__list_of_entries[attempt_no][i].get()
                # If the letter is in the word
                if character.lower() == self.__word_to_guess[k]:
                    # If the position is correct
                    if i == k:
                        self.__list_of_entries[attempt_no][i].config(
                            {"background": "green"}
                        )
                        correct_letters += 1
                        pass
                    # If the position is not correct
                    else:
                        self.__list_of_entries[attempt_no][i].config(
                            {"background": "orange"}
                        )

        # Check if the user has guessed the right word, print out the
        # congratulations message
        if correct_letters == len(self.__list_of_entries[attempt_no]):
            self.__announcement_label.config(
                text="Congratulations! \n "
                     "You have figured out the right word \n with "
                     + str(self.__attempt_no + 1)
                     + " attempts!"
            )

            # Calculate and display the time taken
            end_time = time.time()
            time_taken = end_time - self.__start_time
            self.__end_time = end_time  # Store the end time
            self.__announcement_label.config(
                text=self.__announcement_label.cget("text")
                     + "\nTime Taken: {:.2f} seconds".format(time_taken)
            )

            # Disable the submit button since the word
            # has been correctly guessed
            self.__submit_button.config(state="disabled")

            # Add the score to the leaderboard
            self.add_to_leaderboard(
                self.__user_name,
                len(self.__list_of_entries[attempt_no]),
                self.__attempt_no + 1,
                time_taken,
            )

            return True
        else:
            return False

    def update_time(self):
        """
        This method updates the time taken by the user to guess the word.
        """
        # Check if the time label still exists in the GUI.
        # If not, there is no need to continue updating the time, so return.
        if not self.__time_label.winfo_exists():
            return

        current_time = 0

        # If the start_time is set i.e. the user has started guessing the word
        # and the end_time is not set i.e. the user has not finished guessing,
        # calculate the current time by subtracting the start_time
        # from the current time.
        if self.__start_time and not self.__end_time:
            current_time = time.time() - self.__start_time

        # If the end_time is set , calculate the current time
        # by subtracting the start_time from the end_time.
        elif self.__end_time:
            current_time = self.__end_time - self.__start_time

        # Update the time label in the GUI to show the current time taken.
        self.__time_label.config(
            text="Time: {:.2f} seconds".format(current_time))

        # Schedule the update_time method to be called again
        # after 100 milliseconds. The time label update continuously.
        self.__main_window.after(100, self.update_time)

    def leaderboard_window_display(self):
        """
        This method creates the leaderboard window, which includes the top 10
        entries of the leaderboard. The result is considered using the attempts
        used and time taken.
        """

        # Destroy the main menu frame and replace with a new frame
        self.__main_menu_frame.destroy()

        self.__leaderboard_frame = Frame(self.__main_window)
        self.__leaderboard_frame.pack()

        # Title label
        title_label = Label(
            self.__leaderboard_frame,
            text="Leaderboard",
            font=("Helvetica", 24, "bold")
        )

        # Set the geometry for the title label
        title_label.grid(row=0, column=20, columnspan=3, pady=10)

        leaderboard_entries = self.get_leaderboard_entries()

        # Sort leaderboard entries based on attempts, then time taken
        # in ascending order
        leaderboard_entries.sort(key=lambda x: x["time_taken"])
        leaderboard_entries.sort(key=lambda x: x["attempts"])

        self.display_entries(leaderboard_entries)

    def display_entries(self, leaderboard_entries):
        """
        This method shows the top 10 entries with the best results in the
        Leaderboard section.

        :param leaderboard_entries: dict, all the finishing entries available
        in the file
        """
        # Display only the top 10 entries
        num_entries_to_display = min(len(leaderboard_entries), 10)

        # Display the leaderboard entries
        for i in range(num_entries_to_display):
            entry = leaderboard_entries[i]

            # Rank label
            rank_label = Label(
                self.__leaderboard_frame,
                text="{}. ".format(i + 1),
                font=("Helvetica", 16),
            )
            rank_label.grid(row=i + 1, column=1, padx=(10, 0), pady=5,
                            sticky=W)

            # User label
            user_label = Label(
                self.__leaderboard_frame,
                text="User: {}".format(entry["user_name"]),
                font=("Helvetica", 16),
            )
            user_label.grid(row=i + 1, column=6, pady=5, sticky=W)

            # Letters label
            letters_label = Label(
                self.__leaderboard_frame,
                text="Letters: {}".format(entry["num_letters"]),
                font=("Helvetica", 16),
            )
            letters_label.grid(row=i + 1, column=16, pady=5, sticky=W)

            # Letters label
            attempts_label = Label(
                self.__leaderboard_frame,
                text="Attempts: {}".format(entry["attempts"]),
                font=("Helvetica", 16),
            )
            attempts_label.grid(row=i + 1, column=21, pady=5, sticky=W)

            # Time label
            time_label = Label(
                self.__leaderboard_frame,
                text="Time: {:.2f} seconds".format(entry["time_taken"]),
                font=("Helvetica", 16),
            )
            time_label.grid(row=i + 1, column=29, padx=(0, 10), pady=5,
                            sticky=W)

        # Return button
        return_button = Button(
            self.__leaderboard_frame,
            text="Return to\nmain menu",
            height=3,
            width=10,
            command=lambda: self.return_to_main_menu("leaderboard"),
        )

        # Set the geometry for the return button
        return_button.grid(
            row=num_entries_to_display + 2, column=20, columnspan=4, pady=10
        )

    @staticmethod
    def get_leaderboard_entries():
        """
        This method gets the users' records in the file, stores it in
        a variable and returns a list of leaderboard entries.

        :return leaderboard_entries: all the finishing entries available
        in the file
        """
        leaderboard_entries = []
        # Read leaderboard entries from file and store them in a list
        try:
            with open("leaderboard.txt", "r") as file:
                for line in file:
                    entry_data = line.strip().split(";")
                    if len(entry_data) == 4:
                        leaderboard_entry = {
                            "user_name": entry_data[0],
                            "num_letters": int(entry_data[1]),
                            "attempts": int(entry_data[2]),
                            "time_taken": float(entry_data[3]),
                        }
                        leaderboard_entries.append(leaderboard_entry)
        except FileNotFoundError:
            pass
        return leaderboard_entries

    @staticmethod
    def add_to_leaderboard(user_name, num_letters, attempts, time_taken):
        """
        This method adds the user's score and other information
         to the leaderboard file.

        :param user_name: str,
        :param num_letters: int,
        :param attempts: int, the number of attempts the player has used.
        :param time_taken: float, the time player used to finish the game.
        """

        # Set the user name of the record to "Anonymous" if the user left
        # the user name empty
        if user_name == "":
            user_name = "Anonymous"

        leaderboard_entry = "{};{};{};{:.2f}".format(
            user_name, num_letters, attempts, time_taken
        )

        # Append the leaderboard entry to the leaderboard file
        try:
            with open("leaderboard.txt", "a") as file:
                file.write(leaderboard_entry + "\n")
        except FileNotFoundError:
            pass


def main():
    GUI()


if __name__ == "__main__":
    main()
