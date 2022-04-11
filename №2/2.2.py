num1 = int(input("Введите число 1 : "))
num2 = int(input("Введите число 2 : "))
print(f'Сколько будет {num1} * {num2} ?')
answer = int(input())
if answer == num1 * num2:
    print("Правильно!")
else:
    print(f'Не правильно! {num1} * {num2} = {num1 * num2}')

