from math import floor

word = "radichanton"
lenWord = len(word)


print(f'{word[::3]} - индексы кратны трём')

print(f"{word[:8]} - первые 8 символов")

print(f"{word[floor(lenWord / 2 - 2):floor(lenWord / 2 + 2)]} - четыре символа из центра строки")

print(f'{word[lenWord - 5:]} - пять символов с конца строки')

print(f'{word[::-1]} - в обратном порядке')


