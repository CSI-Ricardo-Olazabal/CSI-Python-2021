import random
word_list = ["string","JSON","boolean","python","fetch upstream","push","integer","array","compile error","print"]
def display_hangman(tries):
    stages = [  """
                    --------
                    |   |
                    |   O
                    |  /|\\
                    |   |
                    |  / \\
                    -
                """,
                """
                    --------
                    |   |
                    |   O
                    |  /|\\
                    |   |
                    |  /
                    -
                """,
                """
                    --------
                    |   |
                    |   O
                    |  /|\\
                    |   |
                    |
                    -
                """,
                """"
                    --------
                    |   |
                    |   O
                    |  /|
                    |   |
                    |
                    -
                """,
                """
                    --------
                    |   |
                    |   O
                    |   |
                    |   |
                    |
                    -
                """,
                """
                    --------
                    |   |
                    |   O
                    |
                    |
                    |
                    -
                """,
                """
                    --------
                    |   |
                    |
                    |
                    |
                    |
                    -
                """
    ]