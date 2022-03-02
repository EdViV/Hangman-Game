import os
import random


def menu():
     print("""██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗    
██║  ██║██╔══██╗████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗████╗  ██║    
███████║███████║██╔██╗ ██║██║  ███╗██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██╔██╗ ██║    
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║    
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    
                                                                                             """)


def hanging_man(trie):

    if trie == 0:
        print("""  +---+
  |   |
      |
      |
      |
      |
=========""")

    if trie == 1:
        print("""  +---+
  |   |
  O   |
      |
      |
      |
=========""")

    if trie == 2:
         print("""  +---+
  |   |
  O   |
  |   |
      |
      |
=========""")


    if trie == 3:
        print("""  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""")

    if trie == 4:
        print("""  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""")

    if trie == 5:
        print("""  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""")

    if trie == 6:
        print("""  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""")


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


def game_sp(option):
    attempts = 0
    trys = "6"
    cont = ""
    generated_word = word_generation(option)
    letters_tried = []

    word_guess = ["_" for letter in generated_word if letter != "\n"]

    word_reference = [letter.upper() for letter in generated_word if letter != "\n"]

    os.system('cls' if os.name == 'nt' else 'clear')

    while word_guess != word_reference and attempts < 6:
        x = "".join(word_guess)

        hanging_man(attempts)
        print(x)
        print("\n")
        print("*********************************************************")
        print("\n")
        print(letters_tried)
        response = input("Adivina una letra: ")

        try:
            if str.isnumeric(response) == True:
                raise TypeError

            if response.upper() not in word_reference:
                attempts += 1
                trys =str(6 - attempts)
                letters_tried.append(response.upper())
                letters_tried.sort()

            for i in range(len(word_reference)):
                if response.upper() == word_reference[i]:
                    word_guess[i] = response.upper()

                    if response not in letters_tried:
                        letters_tried.append(response.upper())
                        letters_tried.sort()

        except TypeError:
            con = input("Por favor ingresa una letra (enter para continuar)")

        os.system('cls' if os.name == 'nt' else 'clear')

    x = "".join(word_guess)

    if word_guess == word_reference:
        print ("La palabra era: " + x )
        print("GANASTE!!!")
    
    if attempts == 6:
        hanging_man(attempts)
        solution = "".join(generated_word)
        print("La palabra era: " + solution )

    cont = input("Quieres jugar de nuevo? (s/n): ")

    if cont.upper() == "S":
        return True

    if cont.upper() == "N":
        return False


def game_en(option):
    attempts = 0
    tries = "6"
    cont = ""
    generated_word = word_generation(option)
    letters_tried = []

    word_guess = ["_" for letter in generated_word if letter != "\n"]

    word_reference = [letter.upper() for letter in generated_word if letter != "\n"]

    os.system('cls' if os.name == 'nt' else 'clear')

    while word_guess != word_reference and attempts < 6:
        x = "".join(word_guess)

        hanging_man(attempts)
        print(x)
        print("\n")
        print("*********************************************************")
        print("\n")
        print(letters_tried)
        response = input("Guess a letter: ")

        try:
            if str.isnumeric(response) == True:
                raise TypeError

            if response.upper() not in word_reference:
                attempts += 1
                tries =str(6 - attempts)
                letters_tried.append(response.upper())
                letters_tried.sort()

            for i in range(len(word_reference)):
                if response.upper() == word_reference[i]:
                    word_guess[i] = response.upper()

                    if response.upper() not in letters_tried:
                        letters_tried.append(response.upper())
                        letters_tried.sort()

        except TypeError:
            con = input("Please enter a letter (Press enter to continue)")

        os.system('cls' if os.name == 'nt' else 'clear')

    x = "".join(word_guess)

    if word_guess == word_reference:
        print ("You found the word: " + x )
        print("YOU WIN!!!")
    
    if attempts == 6:
        hanging_man(attempts)
        solution = "".join(generated_word)
        print("The word was: " + solution )

    cont = input("Do you want to play again? (y/n): ")

    if cont.upper() == "Y":
        return True
        
    if cont.upper() == "N":
        return False


def run():
    y = True

    while y == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu()
        option = int(input("""1.- Español
2.- English
    
Escoge un Lenguaje || Choose a Language: """))

        if option == 1:
            y = game_sp(option)

        if option == 2:
            y = game_en(option)

if __name__ == '__main__':
    run()