import random


def word_generation(language):
    if language == 1:
        with open("./data.txt","r",encoding="utf-8") as f:
            words = [word for word in f]

    elif language == 2:
        with open("./english_data.txt","r") as f:
            words = [word for word in f]
    
    selected_word = random.choice(words)
    print(selected_word)

def run():
    option = int(input("""Choose a language:
    1.- Español
    2.- English"""))

    word_generation(option)


if __name__ == '__main__':
    run()