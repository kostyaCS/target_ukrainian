"""
This module represents the game target but in Ukrainian
"""
import random
from typing import List
import loguru


def generate_grid() -> List[str]:
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


def get_words(f:str, letters:List[str]) -> List[str]:
    """
    Gets the words that suited the following conditions
    """
    list_of_suited_words = []
    with open(f, 'r', encoding='utf-8') as file_with_words:
        for line in file_with_words:
            if 'intj' in line.strip().split()[-1] or 'noninfl' in line.strip().split()[-1]:
                continue
            if 'noun' in line.strip().split()[-1] and\
             len(line.strip().split()[0]) < 5 and line.strip().split()[0][0] in letters:
                list_of_suited_words.append((line.strip().split()[0], 'noun'))
            elif r'/n' in line.strip().split()[-1] and\
             len(line.strip().split()[0]) < 5 and line.strip().split()[0][0] in letters:
                list_of_suited_words.append((line.strip().split()[0], 'noun'))
            elif 'n' in line.strip().split()[-1] and 'j' not in line.strip().split()[-1]\
            and len(line.strip().split()[0]) <= 5 and line.strip().split()[0][0] in letters:
                list_of_suited_words.append((line.strip().split()[0], line.strip().split()[-1]))
            if ('/adj' in line.strip().split()[-1]  or 'adj' in line.strip().split()[-1]) and\
             len(line.strip().split()[0]) <= 5 and line.strip().split()[0][0] in letters:
                list_of_suited_words.append((line.strip().split()[0], 'adjective'))
            if ('/adv' in line.strip().split()[-1]  or 'adv' in line.strip().split()[-1]) and\
             len(line.strip().split()[0]) <= 5 and line.strip().split()[0][0] in letters:
                list_of_suited_words.append((line.strip().split()[0], 'adjective'))
    return list_of_suited_words
