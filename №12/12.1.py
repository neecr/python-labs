from math import pi


class Sphere:
    def __init__(self, radius, x = 1, y = 1, z = 1):
        self.X = x
        self.Y = y
        self.Z = z
        self.R = radius
        self.V = round((4 / 3) * pi * (self.R * self.R * self.R), 2)
        self.S = round(4 * pi * (self.R * self.R), 2)

    def showInfo(self):
        print(f"Радиус - {self.R}, x - {self.X}, y - {self.Y}, z - {self.Z}")

    def getVolume(self):
        return self.V

    def getSquare(self):
        return self.S

    def getRadius(self):
        return self.R

    def getCenter(self):
        return self.X, self.Y, self.Z

    def setRadius(self, radius):
        self.R = radius
        print(f"Новый радиус: {self.R}")

    def setCenter(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
        print(f"Новый центр: {self.X}, {self.Y}, {self.Z}")

    def isPointInside(self, x, y, z):
        if (abs(x - self.X) < self.R) and (abs(y - self.Y) < self.R) and (abs(z - self.Z) < self.R):
            print(f"Точка {x, y, z} лежит")
        else:
            print(f"Точка {x, y, z} не лежит")

    def __del__(self):
        pass


sphere = Sphere(10)

sphere.showInfo()

print(f"Центр: {sphere.getCenter()}, радиус: {sphere.getRadius()}, площадь: {sphere.getSquare()}, объём: {sphere.getVolume()}")

sphere.setCenter(2, 2, 2)
print(sphere.getCenter())

sphere.setRadius(20)
print(sphere.getRadius())

sphere.isPointInside(20, 2, 3)
sphere.isPointInside(30, 0, 0)

