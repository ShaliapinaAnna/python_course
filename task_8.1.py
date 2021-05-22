class Athlete:
    def __init__(self, name, age, coach):
        self.name = name
        self.age = age
        self.coach = coach


class Coach:
    def __init__(self, name, athletes):
        self.name = name
        self.athletes = athletes

    def training(self, athlete):
        if athlete.coach == self.name:
            self.athletes.append(athlete.name)

    def inform(self):
        print(self.name + ' is coach of ' + str(self.athletes).replace('[', '').replace(']', '').replace("'", ''))


athlete_w = Athlete('Alyona Kostornaya', 16, 'Eteri Tutberidze')
athlete_m = Athlete('Mikhail Kolyada', 24, 'Alexey Mishin')
coach1 = Coach('Alexey Mishin', [])

coach1.inform()
coach1.training(athlete_w)
coach1.inform()
coach1.training(athlete_m)
coach1.inform()
