import gallows
import random
from os import system, name
from time import sleep

words = open('words.txt').readlines()
art = open('art.txt').read()


def get_word():
    rand = random.randint(0, len(words))
    return words[rand]


def play():
    word = get_word()[:-1]
    guessed = []
    wrong_guesses = 0
    board = []
    while wrong_guesses < 6:
        show_board(board, word, wrong_guesses)
        guess = input("Guess a letter.\n").lower()
        if guess in guessed:
            print(f"You already guessed {guess}!")
            input("Press any key to continue...")
        else:
            guessed.append(guess)
            if guess in word:
                for letter in word:
                    if letter == guess:
                        board.append(guess)
            else:
                wrong_guesses += 1

        if len(board) == len(word):
            show_board(board, word, wrong_guesses)
            print(f"Congratulations, you won! The word was {word}!")
            break

    if wrong_guesses == 6:
        show_board(board, word, wrong_guesses)
        print(f"Game Over! The word was {word}!")


def show_board(board, word, wrong_guesses):
    clear_screen()
    print(art)
    print(gallows.man[wrong_guesses])
    display = []
    for character in word:
        if character in board:
            display.append(character)
        else:
            display.append('_')
    for character in display:
        print(character, end=" ")
    print("\n")


def clear_screen():
    sleep(0.25)
    print("\n" * 40)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


while True:
    play()
    again = input("\nWould you like to play again? (Y or N)").lower()
    if again == 'n':
        print("\nThanks for playing!")
        break

