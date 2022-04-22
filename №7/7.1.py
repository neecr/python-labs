students = tuple()
for i in range(1, 16):
    students = students + tuple({ i })
print(students)

lastName = tuple(['Авсюкевич', 'Шумель', 'Аниськов', 'Баранов', 'Войтович', 'Волков',
                  'Дубровский', 'Егелявичус', 'Задора', 'Исаков', 'Казимиренко', 'Ковзель',
                  'Корнеенко', 'Костенко', 'Самойлов'])

number = int(input('Введите номер студента: '))
print(lastName[number - 1])

union = students + lastName
print(union)

sl = union[8:18]

print(sl)
