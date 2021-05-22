class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Special(Table):
    def function(self, sport, sportsman):
        self.sport = sport
        self.sportsman = sportsman

    def show_all(self):
        print('You can use it for', self.sport, 'as famous sportsman', self.sportsman)


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print('It is not kitchen table')
        else:
            self.plases = n

    def outplaces(self):
        print(self.plases)


t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplaces()

t_2 = Special(120, 90, 60)
t_2.function('table tennis', 'Timo Ball')
t_2.show_all()
