import random
word_list = ["string","JSON","boolean","python","fetch upstream","push","integer","array","compile error","print"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = false
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print("Theme: python concepts")
    print(display_hangman(tries))
    print(word_completion)
    [print("\n")]
    while not guessed and tries > 0:
        guess = input("Guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha(): 
            if guess is guessed_letters:
                print("You already tried", guess, "!")
            elif guess not in word:
                print("Isn't is in the word :(")
                tries -= 1
                guessed_letters.append(guess)

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