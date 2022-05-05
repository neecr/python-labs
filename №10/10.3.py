file = open("3.txt", "r", encoding = "utf-8")

lines = 0
for line in file:
    lines += 1

file.close()
file = open("3.txt", "r", encoding = "utf-8")

print(f"Всего в файле {lines} строк")

for i in range(1, lines + 1):
    symbols = 0; words = 0; string = ""
    string = (file.readline()).rstrip()
    words = len(string.split(" "))
    symbols = len(string.strip('\n'))
    print(f'{i}-я строка - "{string}" ({words} слов, {symbols} символов)')

file.close()
