from random import randint

mass = [randint(1, 10) for i in range(5)]
# mass.sort()
print(mass)

mostcount = 0

for i in mass:
    count = mass.count(i)
    if count > mostcount:
        mostcount = count
        mostcommon = i

if mostcount == 1:
    print("В массиве нет повторяющихся чисел")
else:
    print(f"Число {mostcommon} - самое частое")
