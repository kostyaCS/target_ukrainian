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
