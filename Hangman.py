# HANGMAN:

import random

# 3 DIFFICULTIES: EASY, MEDIUM, HARD
# SETTING WORD BANKS:
easy = [
    {"word": "ETHICS",
     "hint": "Deciding what is morally right and wrong."},
    {"word": "GOOGLE",
     "hint": "This knows everything!"},
    {"word": "PRIVACY",
     "hint": "Keeping yourself and your personal data safe when off and online."}
]
medium = [
    {"word": "ALGORITHM",
     "hint": "A clear design of how to solve a problem."},
    {"word": "CREATIVITY",
     "hint": "The use of imagination or original ideas to create something."},
    {"word": "FLOWCHART",
     "hint": "A symbolic diagram to a problem solution."}
]
hard = [
    {"word": "COMPUTATIONAL",
     "hint": "'Why' and 'How to' are the essential foci of this type of thinking."},
    {"word": "DECOMPOSITION",
     "hint": "The process of breaking a larger problem down into smaller modular components."},
    {"word": "GENERALISATION",
     "hint": "Adapting solutions to be used to solve a range of problems."}
]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# FUNCTION TO PRIN OUT THE MENU:
def menu():
    print("""
+------------+
|    MENU    |
+------------+
[1] Easy
[2] Medium
[3] Hard
[4] Exit""")


# FUNCTION TO PRINT OUT THE HANGMAN:
def hangmanGraphic(lives):
    match lives:
        case 8:
            pass
        case 7:
            print("--------")
        case 6:
            print("""
        |
        |
        |
        |
        |
        |
        |
--------+""")
        case 5:
            print("""
--------+
        |
        |
        |
        |
        |
        |
--------+""")
        case 4:
            print("""
--------+
    |   |
        |
        |
        |
        |
        |
--------+""")
        case 3:
            print("""
--------+
    |   |
    _   |
   |_|  |
        |
        |
        |
--------+""")
        case 2:
            print("""
--------+
    |   |
    _   |
   |_|  |
    |   |
    |   |
        |
--------+""")
        case 1:
            print("""
--------+
    |   |
    _   |
   |_|  |
   -|-  |
    |   |
        |
--------+""")
        case 0:
            print("""
--------+
    |   |
    _   |
   |_|  |
   -|-  |
    |   |
   /'\  |
--------+""")


exit = False
while not exit:

    # PRINT MENU & GET INPUT:
    exit = False
    menu()
    menuOpt = input("input: ")

    word_list = []
    match menuOpt:
        case "1":
            word_list = easy.copy()
        case "2":
            word_list = medium.copy()
        case "3":
            word_list = hard.copy()
        case "4":
            exit = True

    # IF THE USER DID NOT CHOOSE TO EXIT:
    if not exit:

        # INITIALISATION:
        secret_word = random.choice(word_list)

        word_as_shown = ""  # the word as shown to the user
        for x in range(len(secret_word['word'])):
            word_as_shown += "_"

        abc = alphabet.copy()
        escape = False
        lives = 8

        # GUESSING THE WORD:
        while not escape:

            # PRINT THE WORD & GET USER INPUT:
            print(word_as_shown)
            guess = input("Enter a letter or a ? for a hint: ")

            # COMPUTE USER'S GUESS:
            if guess == "?":
                print(f"Hint: {secret_word['hint']}")
            else:
                guess = guess.upper()
                # if user input is longer than 1 letter, perform computation for each letter input
                for letter in guess:

                    # CHECK IF LETTER HAS ALREADY BEEN GUESSED:
                    valid = False
                    for x in abc:
                        if letter == x:
                            valid = True
                            abc.remove(x)
                    if not valid:
                        print("letter already guessed")

                    # IF LETTER HAS NOT ALREADY BEEN GUESSED:
                    else:
                        if guess in secret_word['word']:
                            # IF LETTER IS CORRECT, SHOW THE LETTER(s) IN THE WORD_AS_SHOWN
                            print("correct")
                            count = 0
                            for x in secret_word['word']:
                                if letter == x:
                                    word_as_shown = word_as_shown[:count] + \
                                        letter+word_as_shown[count+1:]
                                count += 1
                        else:
                            # IF LETTER IS INCORRECT, DECREMENT THE LIVES COUNTER & DISPLAY THE NEW HANGMAN
                            print("incorrect")
                            lives -= 1
                            hangmanGraphic(lives)

                # CHECK IF USER HAS RUN OUT OF LIVES:
                if lives <= 0:
                    print("Game Over!")
                    print(f"The word was: {secret_word['word']}")
                    escape = True

                # CHECK IF THE USER HAS GUESSED ALL THE LETTERS:
                underscore = False
                for x in word_as_shown:
                    if x == '_':
                        underscore = True
                if not underscore:
                    print(secret_word['word'])
                    print("Congratulations, you've guessed the word!")
                    escape = True
