from pandas.core.frame import DataFrame
import pandas as pd

alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_alphabet = {row.letter:row.code for (index, row) in alphabet.iterrows()}

word = input("Enter a word: ").upper()

word_list = [phonetic_alphabet[letter] for letter in word]
print(word_list)