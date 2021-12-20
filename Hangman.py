import random
from words import words_list

def get_word():
    word = random.choice(words_list)
    return word.upper()
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman! This Hangman is about programming and TIQC!")
    print("Tries: " + display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print ("Uhh, you already guessed that letter", guess )
            elif guess not in word:
                print(guess, "Sorry, your guessed letter is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Very well done, you guessed correct!" or "Good Job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Ahem, you have guessed this already: ", guess)
            elif guess != word:
                print (guess, "is not the correct word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = words_list
        else:
            print("Sorry, but this is not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Wow, you guessed the word! You Win! Congrats!!")
    else:
        print("Uhhh...")
        print("Sorry, but you ran out of tries. The word was " + word + ". Maybe next time!")



def display_hangman(tries):
    stages = [
                """
                  --------
                  |      |
                  |      O
                  |     \||/
                  |      ||
                  |     /  \
                  -
                """,

                """
                  --------
                  |      |
                  |      O
                  |     \||/
                  |      |
                  |     /  
                """,

                """
                  --------
                  |      |
                  |      O
                  |     \||/
                  |      |
                  |       
                """,
                """
                  --------
                  |      |
                  |      O
                  |     \||
                  |      |
                  |       
                  -
                """,

                """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |       

                """,

                """
                  --------
                  |      |
                  |      O
                  |     
                  |      
                  |       
                """,

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
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
