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
    os.system('cls' if os.name == 'nt' else 'clear')

    generated_word = word_generation(option)
    attempts = 0
    tries = "6"

    word_guess = ["_" for letter in generated_word if letter != "\n"]
    word_reference = [letter for letter in generated_word                 if letter != "\n"]


    while word_guess != word_reference and attempts < 6:
        x = "".join(word_guess)
        print(x + "                       You have " + tries + " attempts left")
        print("\n")
        response = input("Guess a letter: ")

        if response not in word_reference:
            attempts += 1
            tries =str(6 - attempts)

        for i in range(len(word_reference)):
            if response == word_reference[i]:
                word_guess[i] = response

        os.system('cls' if os.name == 'nt' else 'clear')

    x = "".join(word_guess)

    if word_guess == word_reference:
        print ("You found the word: " + x )
        print("YOU WIN!!!")
    
    if attempts == 6:
        solution = "".join(generated_word)
        print("The word was: " + solution )


def run():
    option = int(input("""1.- Español
2.- English
    
Escoge un Lenguaje || Choose a Language: """))

    game(option)

if __name__ == '__main__':
    run()