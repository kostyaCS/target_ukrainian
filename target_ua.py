"""
This module represents the game target but in Ukrainian
"""
import random

def generate_grid():
    """
    Creates a game board of five Ukrainian letters
    """
    list_of_ukrainian_letters = []
    alphabet = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й',\
     'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    while len(list_of_ukrainian_letters) != 5:
        choice = random.choice(alphabet)
        if choice not in list_of_ukrainian_letters:
            list_of_ukrainian_letters.append(choice)
    return list_of_ukrainian_letters


def get_words(f, letters):
    list_of_suited_words = []
    with open(f, 'r', encoding='utf-8') as file_with_words:
        for line in file_with_words:
            if 'noun' in line.strip().split()[-1] and len(line.strip().split()[0]) < 5:
                print((line.strip().split()[0], line.strip().split()[-1][:line.strip().split()[-1].index(':')]))


get_words('base.lst', ['1'])