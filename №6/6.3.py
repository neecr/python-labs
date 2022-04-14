from random import randint

spisok = []
summ = 0

col = int(input("Сколько столбцов: "))
row = int(input("Сколько строк: "))


for i in range(col):
    spisok.append([randint(0, 9) for j in range(row)])

for i in range(len(spisok)):
    print()
    for j in range(len(spisok[i])):
        print(spisok[i][j], end = " ")
        summ += spisok[i][j]

print(f"\n Среднее арифметическое - {round(summ / (col * row), 2)}")

