# Victor Macedo
# CIS256 Fall 2026)
# Programming Assignment 4

import random

word_list = [
    "banana", "guava", "pineapple", "mango", "apple", "orange"
    ]

play_again = "y"

while play_again == "y":

    word_selection = random.choice(word_list)

    guessed_letters = []

    attempts = 10
    fails = 0

    print("\nIn this game you have to guess the correct word but one letter at a time.")
    print(f"You have a total of {attempts} attempts, to guess the correct word")
    print("Good luck!")

    while fails < attempts:
        display_word = ""

        for letter in word_selection:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\nWord:", " ".join(display_word))
        print(f"Incorrect guess: {fails}/{attempts}")

        if "_" not in display_word:
            print(f"Your guess is correct: {word_selection}")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            continue

        if guess in guessed_letters:
            print("Try a differ letter, You've uncovered this letter already.")
            continue

        if guess in word_selection:
            guessed_letters.append(guess)
            print("Correct guess.")

        else:
            fails += 1
            print("Incorrect letter.")


    if fails == attempts:
        print(f"\nGame Over! The word was: {word_selection}")

    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == "y":
        continue
    else:
        print ("\nThanks for playing!.")
