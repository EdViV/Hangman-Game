import os
import random


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
    guess = []
    check = []
    generated_word = word_generation(option)

    for letter in generated_word:
        check[letter] = letter
        guess[letter] = "_"

    print(check)
    print(guess)

def run():
    option = int(input("""Choose a language:
    1.- Español
    2.- English"""))

    game(option)


if __name__ == '__main__':
    run()