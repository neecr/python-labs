class Computer:
    def __init__(self, mark, diskmemory, ram, cpu):
        self.mark = mark
        self.diskmemory = diskmemory
        self.ram = ram
        self.cpu = cpu

    def changeInfo(self):
        print("======Обновлённые данные======")
        comp.mark = input("Марка - ")
        comp.diskmemory = input("Объем диска - ")
        comp.ram = input("Объеми оперативки - ")
        comp.cpu = input("ЦП - ")

    def showInfo(self):
        print(f"Марка - {comp.mark}")
        print(f"Объём диска - {comp.diskmemory} Gb")
        print(f"Оперативная память - {comp.ram} Gb")
        print(f"Процессор - {comp.cpu}")


    def __del__(self):
        pass


comp = Computer("Asus", 1000, 8, "Intel Core i5")

comp.showInfo()
comp.changeInfo()
comp.showInfo()