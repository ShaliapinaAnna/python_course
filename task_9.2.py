class Figure:
    def __init__(self, color, h, w, l):
        self.color = color
        self.height = h
        self.width = w
        self.long = l

    def coloring(self):
        self.color = 'white'

    def show_all(self):
        print('')


class Oval(Figure):
    def __init__(self, h, w, l, color):
        super().__init__(color, h, w, l)
        if color is None:
            self.color = 'white'

    def show_all(self):
        print("This is {} oval. \n Height: {}. \n Width: {}. \n Lenght: {}.".format(self.color, self.height, self.width, self.long))


class Square(Figure):
    def __init__(self, h, w, l, color):
        super().__init__(color, h, w, l)
        if color is None:
            self.color = 'white'

    def show_all(self):
        print("This is {} square. \n Height: {}. \n Width: {}. \n Lenght: {}.".format(self.color, self.height, self.width, self.long))


oval = Oval(12, 3, 4, 'yellow')
oval.show_all()
square = Square(4, 5, 6, None)
square.show_all()
