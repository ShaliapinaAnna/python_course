class UniversityChecking:
    def __init__(self, st_name, st_homework: list):
        self.st_name = st_name
        self.__st_homework = st_homework

    def st_homework(self, subj):
        if self.__homework_passed(subj):
            return 'it"s my task'
        else:
            return 'i need to do it'

    def __homework_passed(self, subj):
        if subj in self.__st_homework:
            return True
        return False


Anna = UniversityChecking('Anna', ['programming', 'français'])
print('français:', Anna.st_homework('français'))
