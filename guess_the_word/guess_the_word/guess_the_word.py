# Victor Macedo
# CIS256 Fall 2026)
# Programming Assignment 4

# This program is a guessing game where the user has to guess
# a hidden word one letter at a time. 

import random

# preselected list of words the algorith will pick from
word_list = [
    "banana", "guava", "pineapple", "mango", "apple", "orange"
    ]

# Y (yes) will start the game and allow the player to play again
play_again = "y"

while play_again == "y":

    # This is the word selected by the random func
    word_selection = random.choice(word_list)

    # Starts an empty list to save guessed letters
    guessed_letters = []

    # Guesses and attempts available 
    attempts = 10
    fails = 0

    # Start and instructions to the game
    print("\nIn this game you have to guess the correct word but one letter at a time.")
    print(f"You have a total of {attempts} attempts, to guess the correct word")
    print("Good luck!")

    # Loop to continue playing untill user runs out of trys
    while fails < attempts:
        display_word = ""

        for letter in word_selection:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        # Display letters found and attempts remaining
        print("\nWord:", " ".join(display_word))
        print(f"Incorrect guess: {fails}/{attempts}")

        if "_" not in display_word:
            print(f"Your guess is correct: {word_selection}")
            break

        # new letter request     
        guess = input("Enter a letter: ").lower()

        # Error Handling - ignore anything that is not a single letter
        if len(guess) != 1 or not guess.isalpha():
            continue

        # Error handling - avoids counting the same letter twice and requests a diferent entry    
        if guess in guessed_letters:
            print("Try a differ letter, You've uncovered this letter already.")
            continue

        # Appends guesses letteres to guessed_letters
        if guess in word_selection:
            guessed_letters.append(guess)
            print("Correct guess.")

        # incorrect guess tracking 
        else:
            fails += 1
            print("Incorrect letter.")

    # Word revealed once out of attempts
    if fails == attempts:
        print(f"\nGame Over! The word was: {word_selection}")

    # User request for a new game round
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == "y":
        continue
    else:
        print ("\nThanks for playing!.")
