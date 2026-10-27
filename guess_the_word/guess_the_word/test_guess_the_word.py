# Victor Macedo
# CIS256 Fall 2026
# Programming Assignment 4

# Test guess the word game.

import random
import runpy
from pathlib import Path

def test_selected_word_from_predefine_list(monkeypatch, capsys):

    # defening list of words to pick from randomly
    expected_words = [
        "banana", "guava", "pineapple",
        "mango", "apple", "orange"
    ]

    # Empty list started to save words the game used
    selected_lists = []

    # Record words and return a predictable selection
    def choose_word(options):
        selected_lists.append(list(options))
        return "banana"

    # Single simulation test using the word banana
    monkeypatch.setattr(random, "choice", choose_word)
    responses = iter(["b", "a", "n", "n"])
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(responses)
    )

    # validate that the game uses the list of words and game dir
    game_file = Path(__file__).with_name("guess_the_word.py")
    runpy.run_path(str(game_file))

    assert selected_lists[0] == expected_words

    # Correct word verification
    output = capsys.readouterr().out
    assert "Your guess is correct: banana" in output

# Second test - Guessing the correct word
def test_correct_guess(monkeypatch, capsys):
    monkeypatch.setattr(random, "choice", lambda options: "orange")

    # Single simulation test using the word orange
    responses = iter(["o", "r", "a", "n", "g", "e", "n"])
    monkeypatch.setattr(
        "builtins.input", lambda prompt = "": next(responses)
    )

    # validate that the game uses the list of words and game dir
    game_file = Path(__file__).with_name("guess_the_word.py")
    runpy.run_path(str(game_file))

    # Message output from the game 
    output = capsys.readouterr().out
    assert "Correct guess." in output
    assert "Your guess is correct: orange" in output

# Last test using orange
def test_incorrect_guess(monkeypatch, capsys):
    monkeypatch.setattr(random, "choice", lambda options: "orange")
    
    responses = iter(["x", "w", "r", "a", "f", "t", "l", "n", "g", "e", "n"])
    monkeypatch.setattr(
        "builtins.input", lambda prompt="": next(responses)
    )

    # validate that the game uses the list of words and game dir
    game_file = Path(__file__).with_name("guess_the_word.py")
    runpy.run_path(str(game_file))

    # Message output from game stating incorrect word and prints correct word
    output = capsys.readouterr().out
    assert "Incorrect letter." in output
    assert "Your guess is correct: orange" in output


