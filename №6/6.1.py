spisok = [[6, 5, 3], [6, 4, 6], [10, 20, 9]]

for i in range(len(spisok)):
    for j in range(len(spisok[i])):
        if j == 2:
            spisok[i][j] = spisok[i][j-1] + spisok[i][j - 2]


for i in range(len(spisok)):
    print()
    for j in range(len(spisok[i])):
        print(spisok[i][j], end = " ")
