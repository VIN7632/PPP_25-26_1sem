PI = 3.14


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def vertices(self):
        return 0


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def _len(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def area(self):
        a = self._len(self.x1, self.y1, self.x2, self.y2)
        b = self._len(self.x2, self.y2, self.x3, self.y3)
        c = self._len(self.x3, self.y3, self.x1, self.y1)
        p = (a + b + c) / 2
        return round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)

    def perimeter(self):
        return round(
            self._len(self.x1, self.y1, self.x2, self.y2) +
            self._len(self.x2, self.y2, self.x3, self.y3) +
            self._len(self.x3, self.y3, self.x1, self.y1), 2)

    def vertices(self):
        return 3


class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.w = abs(x2 - x1)
        self.h = abs(y2 - y1)

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def vertices(self):
        return 4


class Circle(Shape):
    def __init__(self, x, y, r):
        self.r = r

    def area(self):
        return round(PI * self.r * self.r, 2)

    def perimeter(self):
        return round(2 * PI * self.r, 2)

    def vertices(self):
        return 0


figures = []

n = int(input("Сколько фигур: "))
for _ in range(n):
    parts = input().split()

    try:
        if parts[0] == "triangle":
            figures.append(Triangle(*map(int, parts[1:])))
        elif parts[0] == "rectangle":
            figures.append(Rectangle(*map(int, parts[1:])))
        elif parts[0] == "circle":
            figures.append(Circle(*map(int, parts[1:])))
        else:
            print("Неизвестная фигура")
    except:
        print("Ошибка ввода")

cmd = input("Что посчитать (area / perimeter / vertices): ")

total = 0
for f in figures:
    if cmd == "area":
        total += f.area()
    elif cmd == "perimeter":
        total += f.perimeter()
    elif cmd == "vertices":
        total += f.vertices()
    else:
        print("Неверная команда")
        break

print("Total", cmd + ":", total)

