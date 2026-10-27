# Victor Macedo
# CIS256 Fall 2026
# Programming Assignment 4

# Test guess the word game.


import random
import runpy
from pathlib import Path

def test_selected_word_from_predefine_list(monkeypatch, capsys):

    expected_words = [
        "banana", "guava", "pineapple",
        "mango", "apple", "orange"
    ]

    selected_lists = []

    def choose_word(options):
        selected_lists.append(list(options))
        return "banana"

    monkeypatch.setattr(random, "choice", choose_word)
    responses = iter(["b", "a", "n", "n"])
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(responses)
    )

    game_file = Path(__file__).with_name("guess_the_word.py")
    runpy.run_path(str(game_file))

    assert selected_lists[0] == expected_words

    output = capsys.readouterr().out
    assert "Your guess is correct: banana" in output

def test_correct_guess(monkeypatch, capsys):

    monkeypatch.setattr(random, "choice", lambda options: "orange")

    responses = iter(["o", "r", "a", "n", "g", "e", "n"])
    monkeypatch.setattr(
        "builtins.input", lambda prompt = "": next(responses)
    )
    
    game_file = Path(__file__).with_name("guess_the_word.py")
    runpy.run_path(str(game_file))

    output = capsys.readouterr().out
    assert "Correct guess." in output
    assert "Your guess is correct: orange" in output

def test_incorrect_guess(monkeypatch, capsys):
    monkeypatch.setattr(random, "choice", lambda options: "orange")
    
    responses = iter(["x", "o", "r", "a", "n", "g", "e", "n"])
    monkeypatch.setattr(
        "builtins.input", lambda prompt="": next(responses)
    )

    game_file = Path(__file__).with_name("guess_the_word.py")
    runpy.run_path(str(game_file))

    output = capsys.readouterr().out

    assert "Incorrect letter." in output

    assert "Your guess is correct: orange" in output


