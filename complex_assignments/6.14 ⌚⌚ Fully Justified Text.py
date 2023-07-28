"""
Implement a program that formats text in a fully justified typesetting. What this means is best demonstrated by an example:

The user enters the number of characters that will be printed in one line. The text justification algorithm will divide the text into segments that are shorter than this and then fill in the line to the desired character length by adding space characters in between the words. The space characters are placed so that in the beginning of the line each word spacings contain one space character more than in the end of the line.
The last line of the text won't be filled with extra spaces. It can be shorter than the other lines.
Programming tips:
Use the operators // and % to calculate the number of space characters.
Remember to divide the program into functions!

An example of justified text

Enter text rows. Quit by entering an empty row.
CHAPTER VIII - CONCERNING THOSE WHO HAVE OBTAINED A PRINCIPALITY BY
WICKEDNESS
Although a prince may rise from a private station in two ways, neither
of which can be entirely attributed to fortune or genius, yet it is
manifest to me that I must not be silent on them, although one could be
more copiously treated when I discuss republics. These methods are
when, either by some wicked or nefarious ways, one ascends to the
principality, or when by the favour of his fellow-citizens a private
person becomes the prince of his country. And speaking of the first
method, it will be illustrated by two examples--one ancient, the other
modern--and without entering further into the subject, I consider these
two examples will suffice those who may be compelled to follow them.


Enter the number of characters per line: 50
CHAPTER  VIII - CONCERNING THOSE WHO HAVE OBTAINED
A PRINCIPALITY BY WICKEDNESS Although a prince may
rise  from  a private station in two ways, neither
of  which can be entirely attributed to fortune or
genius,  yet  it is manifest to me that I must not
be  silent  on  them,  although  one could be more
copiously  treated when I discuss republics. These
methods   are  when,  either  by  some  wicked  or
nefarious  ways,  one ascends to the principality,
or  when  by  the  favour of his fellow-citizens a
private  person becomes the prince of his country.
And  speaking  of  the  first  method,  it will be
illustrated  by  two  examples--one  ancient,  the
other  modern--and  without  entering further into
the  subject,  I  consider these two examples will
suffice those who may be compelled to follow them.
"""


def format_text(text, line_length):
    """
    Formats the given text to be fully justified with the given line length.

    :param text: The text to be formatted.
    :param line_length: The length of each line.
    """
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(current_line) + len(word) <= line_length:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = len(word)

    lines.append(current_line)  # Add the last line

    justified_lines = []
    for line in lines[:-1]:
        spaces_to_add = line_length - sum(len(word) for word in line)
        spaces_between_words = len(line) - 1
        if spaces_between_words == 0:
            justified_lines.append(" ".join(line))
        else:
            spaces_per_word = spaces_to_add // spaces_between_words
            extra_spaces = spaces_to_add % spaces_between_words
            justified_line = ""
            for i, word in enumerate(line):
                justified_line += word
                if i < spaces_between_words:
                    justified_line += " " * (
                        spaces_per_word + (1 if i < extra_spaces else 0)
                    )
            justified_lines.append(justified_line)

    # Add the last line without justification
    justified_lines.append(" ".join(lines[-1]))

    return "\n".join(justified_lines)


def main():
    print("Enter text rows. Quit by entering an empty row.")
    text = ""
    while True:
        line = input()
        if line.strip() == "":
            break
        text += line + " "

    line_length = int(input("Enter the number of characters per line: "))
    justified_text = format_text(text, line_length)
    print(justified_text)


if __name__ == "__main__":
    main()
