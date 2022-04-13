spisok = [1, 2, 3, 4, 20, 5, 6, 7]

try:
    spisok[spisok.index(20)] = 200;
    print(spisok)

except ValueError:
    print("Числа 20 нет в списке!")


