file = open('1.txt', "r", encoding = "utf-8")

mass = []

for _ in range(16):
    students = ""
    students = file.readline()
    students = students.split(" ")
    students = [line.rstrip() for line in students]
    students[2] = int(students[2])
    mass.append(students)

file.close()
summ = 0

for i in range(16):
    summ += mass[i][2]
    if mass[i][2] < 3:
        print(f"{mass[i][0]} {mass[i][1]} - оценка {mass[i][2]}")

print(f"Средняя оценка по классу: {round(summ / 16, 2)}")
