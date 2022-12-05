import random
from WORDS_FILE import my_words


def word_selection(my_words):
    rand_select = random.choice(my_words).upper()
    return (rand_select)


def game(rand_select):
    word_length = '_' * len(rand_select)
    guessed = False
    letters_guessed = []
    words_guessed = []
    tries = 6

    #print(rand_select)  #testing
    print("LET THE GAME BEGIN")
    print(display_hangman(tries))
    print(word_length)
    print('\n')

    while not guessed and tries > 0:
        print(tries)
        guess = input("PLEASE GUESS A LETTER OR WORD : ").upper()

        print(guess) #testing

        if len(guess) == 1 and guess.isalpha():
            print("Guess length 1") #testing

            if guess in letters_guessed:
                print("This letter has been guessed " + guess)
                print(letters_guessed) #testing
            elif guess not in rand_select:
                print(guess + " This letter is not in the word")
                tries -= 1
                letters_guessed.append(guess)
                print(letters_guessed) #testing
            else:
                print("WOW YOU GUESSED A RIGHT LETTER ")
                letters_guessed.append(guess)

                print(letters_guessed) #testing

                word_as_list = list(word_length)
                indices = [i for i, letter in enumerate(rand_select) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_length = "".join(word_as_list)

                if '_' not in word_length:
                    guessed = True

                # index_to_update = []
                # for i in rand_select:
                #     if i == guess:
                #         print("my"+i)
                #         index_to_update.append(i)
                #
                # for index in index_to_update:
                #     word_length[index] = guess



        elif len(guess) == len(rand_select) and guess.isalpha():
            print("FULL WORD") #testing

            if guess in words_guessed:
                print("YOU HAVE ENTERED THIS WORD PREVIOUSLY " + guess)
            elif guess != rand_select:
                print("NOT THE CORRECT WORD")
                tries -= 1
                words_guessed.append(guess)
            else:
                guessed = True
                word_length = guess
        else:
            print("OOH TYPE CORRECT ")
            tries -= 1
        print(display_hangman(tries))
        print(word_length)
        print('\n')

    if guessed:
        print("WOW YOU HAVE GUESSED THE WORD: " + word_length)
    else:
        print("YOU HAVE RUN OUT OF THE TURNS SORRY WORD WAS " + rand_select)


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    the_word = word_selection(my_words)
    game(the_word)

    while input("DO U WANNA PLAY AGAIN (Y/N) ").upper() == 'Y':
        the_word = word_selection(my_words)
        game(the_word)


if __name__ == "__main__":
    main()
