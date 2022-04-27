def find_class():
    if user_class in school:
        return school.get(user_class)
    else:
        return 'Такого класса не существует!'


school = {
    '1А': 21,
    '1Б': 25,
    '2В': 30
}

print(school.keys())

user_class = input('Введите класс для получения кол-ва учеников в ней: ')

print(find_class())

school["1A"] += 4

print(school)