import re


def isVowelLetters(user_text):
    return (re.search('[ауоыэяюёие]', user_text))[0]


def count_vowel_letter(user_text):
    dict_user_text = {value: value.count(str(isVowelLetters(user_text))) % 2 for value in text.split()}
    return len(set(value for key, value in dict_user_text.items())) == 1


text = input().lower()
print(f'\n{text}')
try:
    if count_vowel_letter(text):
        print('Парам пам-пам')
    else:
        print('Пам парам')
except TypeError:
    print('no Vowel letters/Cyrillic in the text')
