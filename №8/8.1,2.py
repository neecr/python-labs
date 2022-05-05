def find_class():
    if user_class in school:
        return school.get(user_class)
    else:
        return 'Такого класса не существует!'


school = {
    'A': 21,
    'Б': 25,
    'В': 30
}

print(school.keys())

user_class = input('Введите класс для получения кол-ва учеников в ней: ')

print(find_class())

print(school)