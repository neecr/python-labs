file = open("2.txt", "sphere", encoding = "utf-8")

while True:
    text = input("Введите строку: ")
    if text == "":
        print("Запись завершена")
        break
    file.write(text)
    file.write("\n")

file.close()
