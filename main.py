"""Program - the game "Field of Miracles"""
import random
import re

word_list = ["Orange", "Grape", "Strawberry", "Watermelon", "Pomegranate", "Apricot", "Lemon"]


def game_field(list_w: list):
    """the game "Field of Miracles"""
    word = random.choice(list_w).lower()
    help_text = list(re.sub("[a-z]", "*", word))
    print(word)

    input_number = int(input("Enter the number: "))
    cnt_step = 0

    while cnt_step <= input_number:
        input_text = input("Enter the text or letter: ").lower()

        if input_text == word:
            return "Вітаю, ви вгадали слово"
            # break

        if input_text not in word:
            cnt_step += 1
            print("Такої літери немає")

        for i in range(len(word)):
            if input_text == word[i]:
                help_text[i] = word[i]

        new_text = ""
        for item in help_text:
            new_text += item
        print(new_text)

        if new_text == word:
            return "Вітаю, ви вгадали слово"

        if cnt_step == input_number and new_text != word:
            return "Спроби вгадати слово закінчилися."

    return "Finished"


print(game_field(word_list))
