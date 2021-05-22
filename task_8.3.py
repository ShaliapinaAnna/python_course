class Triangle:
    def __init__(self, color):
        self.color = color


class Circle:
    def __init__(self, color):
        self.color = color


class Square:
    def __init__(self, color):
        self.color = color


class Rhombus:
    def __init__(self, color):
        self.color = color


class Container:
    def __init__(self):
        self.triangles = []
        self.circles = []
        self.squares = []
        self.rhombuses = []

    def show_info(self):
        print(f'There are: {len(self.triangles)} triangle(s) {" and ".join([triangle.color for triangle in self.triangles])}, '
              f'{len(self.circles)} circle(s) {" and ".join([circle.color for circle in self.circles])}, '
              f'{len(self.squares)} square(s) {" and ".join([square.color for square in self.squares])},'
              f'{len(self.rhombuses)} rhombus(es) {" and ".join([rhombus.color for rhombus in self.rhombuses])}.')

    def add_f(self, f):
        if isinstance(f, Triangle):
            self.triangles.append(f)
        elif isinstance(f, Circle):
            self.circles.append(f)
        elif isinstance(f, Square):
            self.squares.append(f)
        else:
            self.rhombuses.append(f)


t1 = Triangle('white')
c1 = Circle('yellow')
s1 = Square('velvet')
s2 = Square('silver')
r1 = Rhombus('green')

cont = Container()

cont.add_f(t1)
cont.add_f(c1)
cont.add_f(s1)
cont.add_f(s2)
cont.add_f(r1)

cont.show_info()
