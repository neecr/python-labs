from random import randint

spisok = []

for i in range(5):
    spisok.append([randint(-3, 3) for j in range(5)])

print("Данный список : ", end = "")

for i in range(len(spisok)):
    print()
    for j in range(len(spisok[i])):
        print(spisok[i][j], end = " ")

print()
summ = 0
for i in range(len(spisok)):
    for j in range(len(spisok[i])):
        if spisok[i][j] < 0: summ += spisok[i][j]

print(f"Сумма отрицательных чисел = { summ }")

