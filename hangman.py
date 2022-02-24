import os
import random


ALPHA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def word_generation(language):
    if language == 1:
        with open("./data.txt","r",encoding="utf-8") as f:
            words = [word for word in f]

    elif language == 2:
        with open("./english_data.txt","r") as f:
            words = [word for word in f]
    
    else:
        print("Please select a given language")

    selected_word = random.choice(words)

    return selected_word


def game (option):
    generated_word = word_generation(option)

    word_guess = ["_" for letter in generated_word if letter != "\n"]
    word_reference = [letter for letter in generated_word                 if letter != "\n"]

    print(word_reference)
    print(word_guess)

    while word_guess != word_reference:
        response = input("Guess a letter: ")

        for i in range(len(word_reference)):
            if response == word_reference[i]:
                word_guess[i] = response

        print(word_reference)
        print(word_guess)


def run():
    option = int(input("""Choose a language:
    1.- Español
    2.- English"""))

    game(option)

if __name__ == '__main__':
    run()