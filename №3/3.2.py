a = int(input("Число mass (mass<b) : "))
b = int(input("Число b : "))

for i in range(a, b + 1):
    print(str(i) * i, end = " ")
