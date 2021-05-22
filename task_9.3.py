class Person:
    def __init__(self, name, company, department, post, experience):
        self.name = name
        self.company = company
        self.department = department
        self.post = post
        self.experience = experience

    def show_info(self):
        print(f"Hello! My name is {self.name}, I'm a {self.post} in {self.department} of {self.company}. My experience is {self.experience} year(s)")


class Director(Person):
    def __init__(self, name, company, department, post, experience, salary, employers):
        super(Director, self).__init__(name, company, department, post, experience)
        self.salary = salary
        self.employers = employers

    def employ(self, new_employer):
        self.employers.append(new_employer)
        print(f'New person: {new_employer.name}, post: {new_employer.post}, salary: {new_employer.salary}')

    def dismiss(self, employer):
        self.employers.remove(employer)
        print(f'{employer.name} is fired, free post: {employer.post}, free money for new person: {employer.salary}')


class Employer(Person):
    def __init__(self, name, age, department, post, experience, salary):
        super().__init__(name, age, department, post, experience)
        self.salary = salary

    def get_hired(self, chef):
        chef.employ(self)
        if self in chef.employers:
            print(f'Now you are in {chef.company}, your chef is {chef.name}.')


chef = Director('Andrew', '2GIS', 'HR', 'Head of everything', 20, 150000, [])
chef.show_info()
work1 = Employer('Anton', 29, 'HR', 'Programmer', 9, 30000)
work2 = Employer('Irina', 25, 'HR', 'SMM', 6, 25000)
work3 = Employer('Makar', 32, 'HR', 'Content-manager', 10, 40000)
work1.show_info()
work2.show_info()
work3.show_info()
work1.get_hired(chef)
work2.get_hired(chef)
work3.get_hired(chef)
chef.dismiss(work3)
